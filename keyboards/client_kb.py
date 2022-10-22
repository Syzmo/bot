from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
mem_button = KeyboardButton("/mem")
music_button = KeyboardButton("/music")
game_button = KeyboardButton("/game")

location_button = KeyboardButton('Share location', request_location=True)
info_button = KeyboardButton('Share info', request_contact=True)

start_markup.add(start_button, quiz_button, mem_button, music_button, game_button)

Direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

direction_a = KeyboardButton("BeckEnd")
direction_d = KeyboardButton("FullStuck")
direction_b = KeyboardButton("FrontEnd")
direction_u = KeyboardButton("UX UI")
direction_c = KeyboardButton("Android")
direction_q = KeyboardButton("IOS")

Direction_markup.add(direction_u, direction_a, direction_b, direction_c, direction_q, direction_d).add(
    KeyboardButton('CANCEL'))


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('ДА'), KeyboardButton('НЕТ'))

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('CANCEL'))
