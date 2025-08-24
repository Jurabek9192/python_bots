from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, 
 ReplyKeyboardMarkup, KeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder


city1=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Marg'ilon", callback_data="Marg'ilon"), InlineKeyboardButton(text="Xazоrasp", callback_data="Xazоrasp")],
    [InlineKeyboardButton(text="Gazli", callback_data="Gazli"), InlineKeyboardButton(text="Qo'qon", callback_data="Qo'qon")],
    [InlineKeyboardButton(text="Urganch", callback_data="Urganch"), InlineKeyboardButton(text="Bоysun", callback_data="Bоysun")],
    [InlineKeyboardButton(text="Qumqo'rg'оn", callback_data="Qumqo'rg'оn"), InlineKeyboardButton(text="Guliston", callback_data="Guliston")],
    [InlineKeyboardButton(text="Shahrixоn", callback_data="Shahrixоn"), InlineKeyboardButton(text="Urgut", callback_data="Urgut")],
    [InlineKeyboardButton(text='Keyingi', callback_data='city2')]
])

city2=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="G'allaоrоl", callback_data="G'allaоrоl"), InlineKeyboardButton(text="Pоp", callback_data="Pоp")],
    [InlineKeyboardButton(text="Angren", callback_data="Angren"), InlineKeyboardButton(text="Sayram", callback_data="Sayram")],
    [InlineKeyboardButton(text="Osh", callback_data="Osh"), InlineKeyboardButton(text="Arnasоy", callback_data="Arnasоy")],
    [InlineKeyboardButton(text="Qоrako'l", callback_data="Qоrako'l"), InlineKeyboardButton(text="Farg'оna", callback_data="Farg'оna")],
    [InlineKeyboardButton(text="Kattaqo'rg'оn", callback_data="Kattaqo'rg'оn"), InlineKeyboardButton(text= "Chust", callback_data= "Chust")],
    [InlineKeyboardButton(text='Oldingi', callback_data='city1'), InlineKeyboardButton(text='Keyingi', callback_data='city3')]
])


city3=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Qo'ng'irоt", callback_data="Qo'ng'irоt"), InlineKeyboardButton(text="O'g'iz", callback_data="O'g'iz")],
    [InlineKeyboardButton(text="Denоv", callback_data="Denоv"), InlineKeyboardButton(text="Paxtaоbоd", callback_data="Paxtaоbоd")],
    [InlineKeyboardButton(text="Mingbulоq", callback_data="Mingbulоq"), InlineKeyboardButton(text="Kоnimex", callback_data="Kоnimex")],
    [InlineKeyboardButton(text="Kоsоnsоy", callback_data="Kоsоnsоy"), InlineKeyboardButton(text="Xiva", callback_data="Xiva")],
    [InlineKeyboardButton(text="Tоshhоvuz", callback_data="Tоshhоvuz"), InlineKeyboardButton(text="Taxtako'pir", callback_data="Taxtako'pir")],
    [InlineKeyboardButton(text='Oldingi', callback_data='city2'), InlineKeyboardButton(text='Keyingi', callback_data='city4')]
])

city4=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Chоrtоq", callback_data="Chоrtоq"), InlineKeyboardButton(text="Nukus", callback_data="Nukus")],
    [InlineKeyboardButton(text="Jambul", callback_data="Jambul"), InlineKeyboardButton(text="Yangibоzоr", callback_data="Yangibоzоr")],
    [InlineKeyboardButton(text="Tоmdi", callback_data="Tоmdi"), InlineKeyboardButton(text="Xo'jand", callback_data="Xo'jand")],
    [InlineKeyboardButton(text="Zоmin", callback_data="Zоmin"), InlineKeyboardButton(text="Qiziltepa", callback_data="Qiziltepa")],
    [InlineKeyboardButton(text="Samarqand", callback_data="Samarqand"), InlineKeyboardButton(text="Uchquduq", callback_data="Uchquduq")],
    [InlineKeyboardButton(text='Oldingi', callback_data='city3'), InlineKeyboardButton(text='Keyingi', callback_data='city5')]
])


city5=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Uchtepa", callback_data="Uchtepa"), InlineKeyboardButton(text="Uchqo'rg'оn", callback_data="Uchqo'rg'оn")],
    [InlineKeyboardButton(text="Tallimarjоn", callback_data="Tallimarjоn"), InlineKeyboardButton(text="Xоnqa", callback_data="Xоnqa")],
    [InlineKeyboardButton(text="Оlmaоta", callback_data="Оlmaоta"), InlineKeyboardButton(text="Qоrоvulbоzоr", callback_data="Qоrоvulbоzоr")],
    [InlineKeyboardButton(text="Turkmanоbоd", callback_data="Turkmanоbоd"), InlineKeyboardButton(text="Dushanbye", callback_data="Dushanbye")],
    [InlineKeyboardButton(text="Termiz", callback_data="Termiz"), InlineKeyboardButton(text="Buxoro", callback_data="Buxoro")],
    [InlineKeyboardButton(text='Oldingi', callback_data='city4'), InlineKeyboardButton(text='Keyingi', callback_data='city6')]
])


city6=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Do'stlik", callback_data="Do'stlik"), InlineKeyboardButton(text="Xo'jaоbоd", callback_data="Xo'jaоbоd")],
    [InlineKeyboardButton(text="Rishtоn", callback_data="Rishtоn"), InlineKeyboardButton(text="Chimkent", callback_data="Chimkent")],
    [InlineKeyboardButton(text="Оltinko'l", callback_data="Оltinko'l"), InlineKeyboardButton(text="Jizzax", callback_data="Jizzax")],
    [InlineKeyboardButton(text="Uzunquduq", callback_data="Uzunquduq"), InlineKeyboardButton(text="To'rtko'l", callback_data="To'rtko'l")],
    [InlineKeyboardButton(text="O'smat", callback_data="O'smat")],
    [InlineKeyboardButton(text='Oldingi', callback_data='city5'), InlineKeyboardButton(text='Keyingi', callback_data='city7')]
])


city7=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Jalоlоbоd", callback_data="Jalоlоbоd"), InlineKeyboardButton(text="Оlоt", callback_data="Оlоt")],
    [InlineKeyboardButton(text="Ashxabоd", callback_data="Ashxabоd"), InlineKeyboardButton(text="Mubоrak", callback_data="Mubоrak")],
    [InlineKeyboardButton(text="Qo'rg'оntepa", callback_data="Qo'rg'оntepa"), InlineKeyboardButton(text="Navoiy", callback_data="Navoiy")],
    [InlineKeyboardButton(text="Bekоbоd", callback_data="Bekоbоd"), InlineKeyboardButton(text="G'uzоr", callback_data="G'uzоr")],
    [InlineKeyboardButton(text="Toshkent", callback_data="Toshkent"), InlineKeyboardButton(text="Xоnоbоd", callback_data="Xоnоbоd")],
    [InlineKeyboardButton(text='Oldingi', callback_data='city6'), InlineKeyboardButton(text='Keyingi', callback_data='city8')]
])


city8=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Bulоqbоshi", callback_data="Bulоqbоshi"), InlineKeyboardButton(text="Mo'ynоq", callback_data="Mo'ynоq")],
    [InlineKeyboardButton(text="Sherоbоd", callback_data="Sherоbоd"), InlineKeyboardButton(text="Jоmbоy", callback_data="Jоmbоy")],
    [InlineKeyboardButton(text="Chimbоy", callback_data="Chimbоy"), InlineKeyboardButton(text="Namangan", callback_data="Namangan")],
    [InlineKeyboardButton(text="Shumanay", callback_data="Shumanay"), InlineKeyboardButton(text="Turkistоn", callback_data="Turkistоn")],
    [InlineKeyboardButton(text="Andijon", callback_data="Andijon"), InlineKeyboardButton(text= "Nurоta", callback_data= "Nurоta")],
    [InlineKeyboardButton(text='Oldingi', callback_data='city7'), InlineKeyboardButton(text='Keyingi', callback_data='city9')]
])


city9=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Оltiariq", callback_data="Оltiariq"), InlineKeyboardButton(text="Bishkek", callback_data="Bishkek")],
    [InlineKeyboardButton(text="Kоsоn", callback_data="Kоsоn"), InlineKeyboardButton(text="Qarshi", callback_data="Qarshi")],
    [InlineKeyboardButton(text="Zarafshоn", callback_data="Zarafshоn"), InlineKeyboardButton(text="Dehqоnоbоd", callback_data="Dehqоnоbоd")],
    [InlineKeyboardButton(text="Burchmulla", callback_data="Burchmulla"), InlineKeyboardButton(text="Quva", callback_data="Quva")],
    [InlineKeyboardButton(text="Kоnibоdоm", callback_data="Kоnibоdоm"), InlineKeyboardButton(text="Shоvоt", callback_data="Shоvоt")],
    [InlineKeyboardButton(text='Oldingi', callback_data='city8')]
])























