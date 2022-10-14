from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import random
import logging


@dp.message_handler(commands=['info'])
async def info_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Ваше имя - {message.from_user.first_name}\n"
                                                 f"Ваше фамилия - {message.from_user.last_name}\n"
                                                 f"полное имя - {message.from_user.full_name}\n"
                                                 f"На данный момент у вас язык - {message.from_user.language_code}\n"
                                                 f"Ваше id - {message.from_user.id}\n")


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Добро пожаловать в телеграмм бот! {message.from_user.full_name}!\n"
                                                 f'Тут есть такие команды как "/info" - информаци о вас\n'
                                                 f'"/quiz" - викторина из 4 вопроса\n'
                                                 f'"/mem" - отправляет прикольные картирки\n'
                                                 f'"/music" - отправляет рандомную музыку')


@dp.message_handler(commands=['music'])
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
    await bot.send_audio(message.from_user.id, music_list)


@dp.message_handler(commands=['mem'])
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


@dp.message_handler(commands=['quiz'])
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
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Гугл о тебе всё знает!!",
        open_period=25,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = 'Основатель Yandex?'
    answers = [
        "Аркадий, Виктор, Андрей",
        "Илья, Елена, Аркадий",
        "Я",
        "Ты?",
        "Мы)",
        "Елена, Ирина, Владимер"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Яндекс тоже следит за тобой...",
        open_period=25,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_2')
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT", callback_data='button_call_3')
    markup.add(button_call_3)

    question = 'Как расшифровывается ООП?'
    answers = [
        "Огромный Орентир Параметра",
        "Очень Офигенный Певец",
        "Организация Операции Пришельцев",
        "Обьектно ориентированное программирование"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Иди учи 2-й месяц)",
        open_period=25,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_3')
async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("NEXT", callback_data='button_call_4')
    markup.add(button_call_4)
    question = 'АТВЕЧААААЙ!'
    answers = [
        'незнаю',
        '5, 8',
        '11, 8',
        '12, 9',
        '0',
    ]
    photo = open('media/задачка.jpeg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="2-й класс...",
    )


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
