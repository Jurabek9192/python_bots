
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
import app.keys as ks
from app.token import url
import aiohttp
from urllib.parse import quote
import logging
from app.token import cities

router=Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Assalamu alekum!', reply_markup=ks.city1)
    

@router.message(F.text)
async def word(message: Message):
    await message.answer('Bu bot sizga nomoz vaqtlarini bilishga yordam beradi.')
    

@router.callback_query(F.data=='city1')
async def city1(callback: CallbackQuery):
    await callback.answer(show_alert=True)
    await callback.message.edit_reply_markup(reply_markup=ks.city1)


@router.callback_query(F.data=='city2')
async def city1(callback: CallbackQuery):
    await callback.answer(show_alert=True)
    await callback.message.edit_reply_markup(reply_markup=ks.city2)


@router.callback_query(F.data=='city3')
async def city3(callback: CallbackQuery):
    await callback.answer(show_alert=True)
    await callback.message.edit_reply_markup(reply_markup=ks.city3)


@router.callback_query(F.data=='city4')
async def city4(callback: CallbackQuery):
    await callback.answer(show_alert=True)
    await callback.message.edit_reply_markup(reply_markup=ks.city4)


@router.callback_query(F.data=='city5')
async def city5(callback: CallbackQuery):
    await callback.answer(show_alert=True)
    await callback.message.edit_reply_markup(reply_markup=ks.city5)
    

@router.callback_query(F.data=='city6')
async def city6(callback: CallbackQuery):
    await callback.answer(show_alert=True)
    await callback.message.edit_reply_markup(reply_markup=ks.city6)


@router.callback_query(F.data=='city7')
async def city7(callback: CallbackQuery):
    await callback.answer(show_alert=True)
    await callback.message.edit_reply_markup(reply_markup=ks.city7)
    

@router.callback_query(F.data=='city8')
async def city8(callback: CallbackQuery):
    await callback.answer(show_alert=True)
    await callback.message.edit_reply_markup(reply_markup=ks.city8)


@router.callback_query(F.data=='city9')
async def city9(callback: CallbackQuery):
    await callback.answer(show_alert=True)
    await callback.message.edit_reply_markup(reply_markup=ks.city9)

    
@router.callback_query()
async def handle_city(callback: CallbackQuery):
    city=callback.data
    
    if city not in cities:
        await callback.message.answer('Bunday shahar topilmadi.')
        return
    
    api_url = f"https://islomapi.uz/api/present/day?region={quote(city)}"
    print(f"Requesting URL: {api_url}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as resp:
                if resp.status !=200:
                    await callback.message.answer('API xatosi.')
                    return
                data=await resp.json()
    except Exception:
        await callback.message.answer("Internet xatosi.")
        return

    times = data.get("times", {})
    date=data.get('date')
    saharlik = times.get("tong_saharlik", "N/A")
    quyosh = times.get("quyosh", "N/A")
    peshin=times.get('peshin', "N/A")
    asr=times.get('asr', "N/A")
    shom=times.get('shom_iftor', "N/A")
    hufton=times.get('hufton', "N/A")

    await callback.message.answer(
        f"""📍 <b>{city}</b>\n
        {date} sana uchun vaqtlar\n
        Saharlik:  {saharlik}\n
        Quyosh:    {quyosh}\n
        Peshin:    {peshin}\n
        Asr:       {asr}\n
        Shom:      {shom}\n
        Hufton:    {hufton}""",
        parse_mode="HTML"
    )


