from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


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


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')
    dp.register_callback_query_handler(quiz_4, lambda call: call.data == 'button_call_3')