import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_KEY = os.getenv("WEATHER_API_KEY")

print(BOT_TOKEN)
print(WEATHER_KEY)

import telebot
import requests



bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """<b>Assalamu alaykum!</b> 👋
Bu <b>ob-havo boti</b>.
Siz botga shahar nomini yuboring,
va bot sizga shahar <i>ob-havo ma'lumotini</i> yuboradi.

<u>Masalan:</u> <code>Toshkent</code>""",
    parse_mode="HTML")
    
@bot.message_handler(commands=['help'])
def sen_help(message):
    bot.reply_to(message, "Bu bot faqat ob-havo ma'lumotlarini bera oladi")

@bot.message_handler(content_types=['text'])  # Handles all text messages
def get_weather(message):
    city = message.text.strip()
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        bot.reply_to(message, f"❌ Shahar nomi topilmadi iltimos boshqa nomni kiritib ko'ring")
        return

    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    weather_text = (
        f"🌍 Shahar: {city}\n"
        f"🌡 Daraja: {temp}°C (aslida {feels_like}°C kabi bo'lishi mumkin)\n"
        f"💨 Shamol tezligi: {wind_speed} m/s\n"
        f"☁️ Vaziyat: {description}"
    )

    bot.reply_to(message, weather_text)

@bot.message_handler(content_types=['video', 'music', 'sticker', 'text'
    'audio',         # Audio files (MP3, etc.)
    'document',      # Any kind of file
    'photo',         # Images
    'sticker',       # Stickers
    'video',         # Videos
    'video_note',    # Round video messages
    'voice',         # Voice messages
    'location',      # Location (lat/lon)
    'contact',       # Shared contact
    'venue',         # Location with title/address
    'animation',     # GIFs
    'dice',          # Dice and other random emoji games 🎲
    'poll'])
def response(message):
    bot.reply_to(message, "Bu bot faqat ob-havo ma'lumotlari\nuchun mo'ljallangan iltimos shahar nomini yuboring")

# Start bot
print("Bot is running...")
bot.infinity_polling()
