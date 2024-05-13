from aiogram import Router, types
from aiogram.enums import ChatAction
from aiogram.utils.chat_action import ChatActionSender
from aiogram.enums import ParseMode
from bot.main.main_function import nec_info
from bot.keyboard.inline_keyboard import url_info_kb
import random
import settings
from database import db

router = Router(name=__name__)


@router.message()
async def film_info(message: types.Message):
    action_sender = ChatActionSender(bot=message.bot,
                                     chat_id=message.chat.id,
                                     interval=2,
                                     action=ChatAction.UPLOAD_PHOTO)
    user = await db.get_user_id(user_id=message.from_user.id)
    if user is None:
        await db.add_new_user(user_id=message.from_user.id)
    else:
        print(message.text)
        with open('wordlist.txt', 'r', encoding="utf-8") as check:
            zalupa = check.readlines()
            if any(elem+'\n' in zalupa for elem in message.text.lower().split()):
                await message.answer('пашел нахой')
            else:
                async with action_sender:
                    info = await nec_info(message=message.text)
                    if info == 1:
                        await message.answer(text='я не знаю такого фильма')
                    elif info == 2:
                        await message.answer(text='К сожалению у меня нет информации об этом фильме')
                    else:
                        await db.add_film(user_id=message.from_user.id,
                                          film_id=info["film_id"]
                                          )
                        print(info['name'])
                        if info["film_or_serial"]:
                            film_type = 'Средняя длина серии'
                        else:
                            film_type = 'Длина фильма'
                        text = (
                            f'<b>{info["name"]} {info["age_limits"] + "+" if info["age_limits"] is not None else ""} ({info["country"]})</b>'
                            f'\n<b>• Дата выхода: </b>{info["year"]}'
                        )
                        if info["length"] is not None:
                            text += f'\n<b>• {film_type}: </b> {str(info["length"])} мин'
                        if info["ratings"]:
                            text += '\n<b>• Рейтинги: </b>\n   ' + "\n   ".join(
                                [elem["rate"] for elem in info["ratings"]])
                        if info["genres"]:
                            text += f'\n<b>• Жанры: </b>{", ".join([elem["genre"] for elem in info["genres"]])}'
                        if info["short_description"] is not None:
                            text += f'\n<b>• Описание: </b>{info["short_description"]}.'
                        photo_message = await message.answer_photo(photo=info['poster_url'],
                                                                   caption=text,
                                                                   parse_mode=ParseMode.HTML,
                                                                   reply_markup=await url_info_kb(message))
                        photo_id = photo_message.photo[-1].file_id
                        await db.add_film_info(user_id=message.from_user.id,
                                               film_name=info["name"],
                                               film_pic_id=photo_id,
                                               film_info=text,
                                               film_description=info["description"],
                                               film_name_etc=f'{info["name"]} {info["age_limits"] + "+" if info["age_limits"] is not None else ""} ({info["country"]})\n'
                                               )
