from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot

from keyboards import kb_menu, kb_colomn

all = None


class Followup(StatesGroup):
    type = State()
    chat = State()
    date = State()
    who = State()
    done = State()
    todo = State()
    discuss = State()


async def command_menu(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Запутался?)', reply_markup=kb_menu)
    await state.finish()


# Управление роботом
async def command_robot_control(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выбери ячейки для разкрузки', reply_markup=kb_colomn)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_robot_control, lambda message: 'Серега молодец' in message.text, state=None)
#    dp.register_message_handler(command_followup, lambda message: "\U0001F4DDFollow-up" in message.text, state=None)
#    dp.register_message_handler(command_menu, lambda message: "Main menu" in message.text, state=Sprints.all_states)
#    dp.register_message_handler(command_tasks, state=None)

#    dp.register_message_handler(command_sprint_done, state=Sprints.done)
 #   dp.register_message_handler(command_sprint_todo, state=Sprints.todo)
  #dp.register_message_handler(command_followup_todo, state=Followup.todo)
   # dp.register_message_handler(command_followup_discuss, state=Followup.discuss)