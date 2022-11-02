from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp, ADMINS
import random
from keyboards.client_kb import start_markup
from Database.bot_db import sql_command_random
from parser.film import parser


async def dice_game(message: types.Message):
    a = await bot.send_dice(message.chat.id)
    b = await bot.send_dice(message.chat.id)
    if a.dice.value > b.dice.value:
        await bot.send_message(message.chat.id, 'ты выиграл бота!')
    elif a.dice.value < b.dice.value:
        await bot.send_message(message.chat.id, 'ты проиграл бота ха-ха!')


async def game_message(message: types.Message):
    if message.from_user.id in ADMINS:
        data = ['🎲', '⚽️', '🎳', '🏀', '🎯', '🎰']
        r = random.choice(data)
        await bot.send_dice(message.chat.id, emoji=r)
    else:
        await bot.send_message(message.chat.id, 'У тебя не достаточно прав!')


async def pin_message(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer("Укажи что закрепить!")


async def info_command(message: types.Message):
    await bot.send_message(message.chat.id, f"Ваше имя - {message.from_user.first_name}\n"
                                            f"Ваше фамилия - {message.from_user.last_name}\n"
                                            f"полное имя - {message.from_user.full_name}\n"
                                            f"На данный момент у вас язык - {message.from_user.language_code}\n"
                                            f"Ваше id - {message.from_user.id}\n")


async def start_command(message: types.Message):
    await bot.send_message(message.chat.id, f"Добро пожаловать в телеграмм бот! {message.from_user.full_name}!\n"
                                            f'Тут есть такие команды как:\n'
                                            f'"/game" - рандомная встроенная мини-игра(только для админов)\n'
                                            f' "/info" - информаци о вас\n'
                                            f'"/quiz" - викторина из 4 вопроса\n'
                                            f'"/mem" - отправляет прикольные картирки\n'
                                            f'"/music" - отправляет рандомную музыку',
                           reply_markup=start_markup)




async def parser_film(message: types.Message):
    items = parser()
    for item in items:
        await message.answer(
            f"{item['link']}\n\n"
            f"{item['title']}\n"
            f"#Y{item['year']}\n"
            f"#{item['city']}\n"
            f"#{item['genre']}"
        )


async def music(message: types.Message):
    music_list = open('audio/DaBro - Мне Не Страшно.mp3', 'rb')
    numbers = random.randint(1, 6)
    if numbers == 1:
        music_list = open('audio/Eva Rida - Лови Лови.mp3', 'rb')
    if numbers == 2:
        music_list = open('audio/poly-brige-shrek-igraet-na-saksofone.mp3', 'rb')
    if numbers == 3:
        music_list = open('audio/St Project - The Night.mp3', 'rb')
    if numbers == 4:
        music_list = open('audio/Песня - А если пиво чуть прохладное это фантастик_[mp3mob.net].mp3', 'rb')
    if numbers == 5:
        music_list = open('audio/Нкей - Толпы Кричат.mp3', 'rb')
    if numbers == 6:
        music_list = open('audio/miyagi-samuraj(mp3name.co).mp3', 'rb')
    await bot.send_audio(message.chat.id, music_list)


async def mems(message: types.Message):
    mem_photo = open("media/mems2.jpeg", "rb")
    number = random.randint(1, 8)
    if number == 1:
        mem_photo = open("media/mems1.jpeg", "rb")
    if number == 2:
        mem_photo = open("media/mems.jpeg", "rb")
    if number == 3:
        mem_photo = open('media/CatMemes_PreviewVert.jpeg', 'rb')
    if number == 4:
        mem_photo = open('media/mems3.jpeg', 'rb')
    if number == 5:
        mem_photo = open('media/mems4.jpeg', 'rb')
    if number == 6:
        mem_photo = open('media/mems5.jpeg', 'rb')
    if number == 7:
        mem_photo = open('media/mems6.jpeg', 'rb')
    if number == 8:
        mem_photo = open('media/mems7.jpeg', 'rb')
    await bot.send_photo(message.chat.id, mem_photo)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'В каком году был создан Google?'
    answers = [
        '1998',
        "1989",
        "1996",
        "2001",
        "2000",
        "2003"
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Гугл о тебе всё знает!!",
        open_period=25,
        reply_markup=markup
    )


async def get_random_user(message: types.Message):
    await sql_command_random(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(info_command, commands=['info'])
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(music, commands=['music'])
    dp.register_message_handler(mems, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin_message, commands=['pin'])
    dp.register_message_handler(game_message, commands=['game'])
    dp.register_message_handler(dice_game, commands=['dice'])
    dp.register_message_handler(get_random_user, commands=['dice'])
    dp.register_message_handler(parser_film, commands=['film'])
