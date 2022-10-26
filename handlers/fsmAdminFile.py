from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from Database.bot_db import sql_command_insert
from config import bot, ADMINS
from keyboards.client_kb import Direction_markup, cancel_markup, submit_markup


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    grup = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMINS:

        await FSMAdmin.id.set()
        await message.answer(f"привет, {message.from_user.full_name}\n"
                             f'напишите ID ментора', reply_markup=cancel_markup)
    elif message.from_user.id not in ADMINS:
        await message.answer('ты не являешься куратором')
    else:
        await message.answer('Пиши в личку!')


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
         data['id'] = int(message.text)
    await FSMAdmin.next()
    await message.answer("Какое имя у ментора? ")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Какие направление у ментора?", reply_markup=Direction_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Возраст ментора", reply_markup=cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await FSMAdmin.next()
    await message.answer("какая группа?")


async def load_grup(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['grup'] = message.text
        await message.answer(f"ID: {data['id']}\n"
                               f"Имя: {data['name']}\n"
                               f"Направление: {data['direction']}\n"
                               f"Возраст: {data['age']}\n"
                               f"Группа: {data['grup']}")

    await FSMAdmin.next()
    await message.answer("Все правильно?", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Регистрация завершена")
    if message.text.lower() == 'нет':
        await state.finish()
        await message.answer("Отмена")


async def cancel_reg(message: types.Message, state: FSMContext):
    curren_state = await state.get_state()
    if curren_state is not None:
        await state.finish()
        await message.answer("Вы вышли из регистрации анкеты!")


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')

    dp.register_message_handler(fsm_start, commands=['anketa'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_grup, state=FSMAdmin.grup)
    dp.register_message_handler(submit, state=FSMAdmin.submit)