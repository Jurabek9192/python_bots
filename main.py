# main.py
import os
import time
import logging
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_KEY = os.getenv("WEATHER_API_KEY")

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import telebot
from telebot import apihelper

# ---- Basic checks ----
if not BOT_TOKEN:
    raise SystemExit("ERROR: BOT_TOKEN is not set in environment.")
if not WEATHER_KEY:
    raise SystemExit("ERROR: WEATHER_API_KEY is not set in environment.")

# ---- Logging ----
logger = logging.getLogger("weather_bot")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Starting bot...")

# ---- Requests session with retries ----
session = requests.Session()
retries = Retry(
    total=5,
    backoff_factor=1,                 # exponential backoff: 1s, 2s, 4s...
    status_forcelist=(429, 500, 502, 503, 504),
    allowed_methods=frozenset(["GET", "POST"])  # allow retries for GET/POST
)
adapter = HTTPAdapter(max_retries=retries)
session.mount("https://", adapter)
session.mount("http://", adapter)

# It's helpful for telebot to use a custom request session for external calls.
# telebot uses its own internal HTTP calls to Telegram; we will still catch exceptions around bot replies.

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# ---- Helpers ----
def fetch_weather_for_city(city: str, timeout: int = 10):
    """Return dict on success or tuple (False, message) on failure."""
    try:
        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={requests.utils.quote(city)}&appid={WEATHER_KEY}&units=metric&lang=uz"
        )
        logger.info("Requesting weather for %s", city)
        resp = session.get(url, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        # openweathermap uses 'cod' as int or str
        if str(data.get("cod")) != "200":
            logger.warning("Weather API returned non-200 code for %s: %s", city, data.get("cod"))
            return False, "Shahar topilmadi yoki API javobida muammo bor."
        return True, data
    except requests.exceptions.RequestException as e:
        logger.error("RequestException while fetching weather for %s: %s", city, e)
        return False, "Tarmoq xatosi yuz berdi. Iltimos keyinroq urinib ko'ring."

def safe_reply(message_obj, text, **kwargs):
    """Reply safely: catch exceptions so bot doesn't crash from send errors."""
    try:
        bot.reply_to(message_obj, text, **kwargs)
    except Exception as e:
        # Log the exception but do not crash
        logger.exception("Failed to send message to chat %s: %s", getattr(message_obj, "chat", None), e)

# ---- Handlers ----
@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = (
        "<b>Assalamu alaykum!</b> 👋\n"
        "Bu <b>ob-havo boti</b>.\n"
        "Siz botga shahar nomini yuboring, va bot sizga shahar <i>ob-havo ma'lumotini</i> yuboradi.\n\n"
        "<u>Masalan:</u> <code>Toshkent</code>"
    )
    safe_reply(message, text, parse_mode="HTML")

@bot.message_handler(commands=['help'])
def send_help(message):
    safe_reply(message, "Bu bot faqat ob-havo ma'lumotlarini beradi. Shahar nomini yuboring.")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip()
    if not city:
        safe_reply(message, "Iltimos shahar nomini yuboring.")
        return

    ok, result = fetch_weather_for_city(city)
    if not ok:
        safe_reply(message, f"❌ {result}")
        return

    data = result
    try:
        temp = data["main"]["temp"]
        feels_like = data["main"].get("feels_like", temp)
        description = data["weather"][0].get("description", "—")
        wind_speed = data.get("wind", {}).get("speed", "—")

        weather_text = (
            f"🌍 Shahar: {city}\n"
            f"🌡 Hozirgi harorat: {temp}°C\n"
            f"🤔 His etilishi: {feels_like}°C\n"
            f"💨 Shamol tezligi: {wind_speed} m/s\n"
            f"☁️ Vaziyat: {description}"
        )
    except Exception as e:
        logger.exception("Error parsing weather response for %s: %s", city, e)
        safe_reply(message, "API javobini qayta ishlashda xato yuz berdi.")
        return

    safe_reply(message, weather_text)

# Handler for non-text content — respond with a short message
NON_TEXT_TYPES = [
    'video', 'music', 'sticker', 'audio', 'document', 'photo',
    'video_note', 'voice', 'location', 'contact', 'venue',
    'animation', 'dice', 'poll'
]

@bot.message_handler(content_types=NON_TEXT_TYPES)
def non_text_response(message):
    safe_reply(message, "Bu bot faqat ob-havo ma'lumotlari uchun mo'ljallangan — iltimos shahar nomini matn shaklida yuboring")

# ---- Resilient polling loop ----
def run_polling_loop():
    # tune these values if you need
    timeout = 20  # Telegram long polling timeout in seconds
    long_polling_timeout = 60

    while True:
        try:
            logger.info("Starting infinity_polling()")
            # infinity_polling itself wraps polling loop, but we protect the outer loop to catch any unexpected exceptions
            bot.infinity_polling(timeout=timeout, long_polling_timeout=long_polling_timeout)
        except KeyboardInterrupt:
            logger.info("KeyboardInterrupt received, exiting.")
            break
        except Exception as e:
            logger.exception("Unhandled exception in polling loop: %s", e)
            # sleep to avoid tight crash loop; exponential backoff could be used here
            time.sleep(5)

if __name__ == "__main__":
    run_polling_loop()
