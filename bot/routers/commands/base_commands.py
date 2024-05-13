from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.utils.formatting import Text, Bold
from aiogram.enums import ChatAction
from aiogram.utils.chat_action import ChatActionSender
from database import db

router = Router(name=__name__)


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    action_sender = ChatActionSender(bot=message.bot,
                                     chat_id=message.chat.id,
                                     action=ChatAction.TYPING)
    async with action_sender:
        user = await db.get_user_id(user_id=message.from_user.id)
        if user is None:
            await db.add_new_user(user_id=message.from_user.id)
        content = Text(
            "Привет, ", Bold(message.from_user.full_name),
            ', я бот который отправит тебе информацию о фильме и ссылку на просмотр\n\n'
            'Если что-то не получается - /help\n\n'
            'Для дальнейшего взаимодействия с ботом, просто отправьте полное название фильма'
        )
        await message.answer(
            **content.as_kwargs()
        )


@router.message(Command('help'))
async def cmd_help(message: types.Message):
    action_sender = ChatActionSender(bot=message.bot,
                                     chat_id=message.chat.id,
                                     action=ChatAction.TYPING)
    async with action_sender:
        await message.answer(text='Здесь рассмотрены возможные проблемы:\n\n'
                                  '•  Если вы не можете найти нужный вам фильм - либо его нет, либо он еще не вышел\n'
                                  '•  Если на сайте не открывается фильм - возможно такого фильма нет в базе, либо он еще не вышел')
