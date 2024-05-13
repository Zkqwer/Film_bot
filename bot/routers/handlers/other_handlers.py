import random
from aiogram import Router, types
from aiogram.enums import ChatAction
from aiogram.utils.chat_action import ChatActionSender
import settings

router = Router(name=__name__)


@router.message(settings.any_media_filter)
async def user_send_not_text(message: types.Message):
    action_sender = ChatActionSender(bot=message.bot,
                                     chat_id=message.chat.id,
                                     action=ChatAction.CHOOSE_STICKER)
    async with action_sender:
        await message.answer_sticker(random.choice(settings.stickers))
