from aiogram import Router, F, types, exceptions
from aiogram.utils.media_group import MediaGroupBuilder
from bot.keyboard.inline_keyboard import info_kb, url_info_kb
from aiogram.enums import ChatAction
from aiogram.utils.chat_action import ChatActionSender
from database import db
from bot.main import main_function as m_func
from aiogram.enums import ParseMode

router = Router(name=__name__)


@router.callback_query(F.data == 'info')
async def film_info(callback_query: types.CallbackQuery):
    action_sender = ChatActionSender(bot=callback_query.message.bot,
                                     chat_id=callback_query.message.chat.id,
                                     interval=1,
                                     action=ChatAction.TYPING)
    async with action_sender:
        await callback_query.answer()
        message = await callback_query.bot.edit_message_media(chat_id=callback_query.message.chat.id,
                                                              message_id=callback_query.message.message_id,
                                                              media=types.InputMediaPhoto(
                                                                  media=await db.get_film_pic_id(
                                                                      user_id=callback_query.from_user.id
                                                                  ),
                                                                  caption=await db.get_film_name_etc(
                                                                      user_id=callback_query.from_user.id
                                                                  ),
                                                                  parse_mode=ParseMode.HTML
                                                              ),
                                                              reply_markup=await info_kb()
                                                              )
        await db.add_message_delete_id(message_delete_id=message.message_id, user_id=callback_query.from_user.id)


@router.callback_query(F.data == 'back')
async def handle_info(callback_query: types.CallbackQuery):
    action_sender = ChatActionSender(bot=callback_query.message.bot,
                                     chat_id=callback_query.message.chat.id,
                                     interval=1,
                                     action=ChatAction.TYPING)
    async with action_sender:
        await callback_query.answer()
        await callback_query.bot.edit_message_media(chat_id=callback_query.message.chat.id,
                                                    message_id=callback_query.message.message_id,
                                                    media=types.InputMediaPhoto(
                                                        media=await db.get_film_pic_id(
                                                            user_id=callback_query.from_user.id
                                                        ),
                                                        caption=await db.get_film_info(
                                                            user_id=callback_query.from_user.id
                                                        ),
                                                        parse_mode=ParseMode.HTML
                                                    ),
                                                    reply_markup=await url_info_kb(
                                                        message=callback_query
                                                    )
                                                    )


@router.callback_query(F.data == 'money')
async def money_info(callback_query: types.CallbackQuery):
    action_sender = ChatActionSender(bot=callback_query.message.bot,
                                     chat_id=callback_query.message.chat.id,
                                     interval=1,
                                     action=ChatAction.TYPING)
    async with action_sender:
        try:
            await callback_query.answer()
            await callback_query.bot.edit_message_media(chat_id=callback_query.message.chat.id,
                                                        message_id=callback_query.message.message_id,
                                                        media=types.InputMediaPhoto(
                                                            media=await db.get_film_pic_id(
                                                                user_id=callback_query.from_user.id
                                                            ),
                                                            caption=await db.get_film_name_etc(
                                                                user_id=callback_query.from_user.id
                                                            ) + '\n' + await m_func.money(
                                                                message=await db.get_film_name(
                                                                    user_id=callback_query.from_user.id
                                                                )
                                                            )
                                                        ),
                                                        reply_markup=await info_kb()
                                                        )
        except exceptions.TelegramBadRequest:
            await callback_query.answer()


@router.callback_query(F.data == 'awards')
async def awards_info(callback_query: types.CallbackQuery):
    action_sender = ChatActionSender(bot=callback_query.message.bot,
                                     chat_id=callback_query.message.chat.id,
                                     interval=1,
                                     action=ChatAction.TYPING)
    async with action_sender:
        try:
            await callback_query.answer()
            await callback_query.bot.edit_message_media(chat_id=callback_query.message.chat.id,
                                                        message_id=callback_query.message.message_id,
                                                        media=types.InputMediaPhoto(
                                                            media=await db.get_film_pic_id(
                                                                user_id=callback_query.from_user.id
                                                            ),
                                                            caption=await db.get_film_name_etc(
                                                                user_id=callback_query.from_user.id
                                                            ) + '\n' + await m_func.awards(
                                                                message=await db.get_film_name(
                                                                    user_id=callback_query.from_user.id
                                                                )
                                                            )
                                                        ),
                                                        reply_markup=await info_kb()
                                                        )
        except exceptions.TelegramBadRequest:
            await callback_query.answer()


@router.callback_query(F.data == 'similar_films')
async def handle_info(callback_query: types.CallbackQuery):
    data = await m_func.similar_movies(
        message=await db.get_film_name(
            user_id=callback_query.from_user.id
        )
    )
    if data == 'Похожих фильмов не найдено' or data == 'Нет информации об этом фильме':
        action_sender = ChatActionSender(bot=callback_query.message.bot,
                                         chat_id=callback_query.message.chat.id,
                                         interval=1,
                                         action=ChatAction.TYPING)
        async with action_sender:
            try:
                await callback_query.bot.edit_message_media(chat_id=callback_query.message.chat.id,
                                                            message_id=callback_query.message.message_id,
                                                            media=types.InputMediaPhoto(
                                                                media=await db.get_film_pic_id(
                                                                    user_id=callback_query.from_user.id
                                                                ),
                                                                caption=await db.get_film_name_etc(
                                                                    user_id=callback_query.from_user.id
                                                                ) + '\n' + data
                                                            ),
                                                            reply_markup=await info_kb()
                                                            )
            except exceptions.TelegramBadRequest:
                await callback_query.answer()
    else:
        action_sender = ChatActionSender(bot=callback_query.message.bot,
                                         chat_id=callback_query.message.chat.id,
                                         interval=1,
                                         action=ChatAction.UPLOAD_PHOTO)
        async with action_sender:
            album_builder = MediaGroupBuilder(
                caption=f'Фильмы похожие на "{await db.get_film_name(user_id=callback_query.from_user.id)}":\n\n'
                        + '\n'.join(f'{i + 1}. {data[i]["name"]}' for i in range(len(data))
                                    )
            )
            for i in range(len(data)):
                album_builder.add_photo(
                    media=data[i]['url']
                )
            await callback_query.bot.delete_message(chat_id=callback_query.from_user.id,
                                                    message_id=await db.get_message_delete_id(
                                                        user_id=callback_query.from_user.id
                                                    )
                                                    )
            await callback_query.message.answer_media_group(
                media=album_builder.build()
            )

    """
        async def info_handler(callback_query):
            message = await callback_query.answer(media=types.InputMediaPhoto(media=
                                                                              await db.get_film_pic_id(
                                                                                  user_id=callback_query.from_user.id),
                                                                              caption=await db.get_film_info(
                                                                                  user_id=callback_query.from_user.id),
                                                                              parse_mode=ParseMode.HTML),
                                                  reply_markup=await info_kb()
                                                  )
            await db.add_message_delete_id(message_delete_id=message.message_id)
    """


@router.callback_query(F.data == 'pics')
async def handle_info(callback_query: types.CallbackQuery):
    data = await m_func.images(
        message=await db.get_film_name(
            user_id=callback_query.from_user.id
        )
    )
    if data == 'Нет информации об этом фильме' or data == 'К сожалению нет информации о фото к данному фильму':
        action_sender = ChatActionSender(bot=callback_query.message.bot,
                                         chat_id=callback_query.message.chat.id,
                                         interval=1,
                                         action=ChatAction.TYPING)
        async with action_sender:
            try:
                await callback_query.bot.edit_message_media(chat_id=callback_query.message.chat.id,
                                                            message_id=callback_query.message.message_id,
                                                            media=types.InputMediaPhoto(
                                                                media=await db.get_film_pic_id(
                                                                    user_id=callback_query.from_user.id
                                                                ),
                                                                caption=await db.get_film_name_etc(
                                                                    user_id=callback_query.from_user.id
                                                                ) + '\n' + data
                                                            ),
                                                            reply_markup=await info_kb()
                                                            )
            except exceptions.TelegramBadRequest:
                await callback_query.answer()
    else:
        action_sender = ChatActionSender(bot=callback_query.message.bot,
                                         chat_id=callback_query.message.chat.id,
                                         interval=1,
                                         action=ChatAction.UPLOAD_PHOTO)
        async with action_sender:
            album_builder = MediaGroupBuilder(
                caption=f'Кадры из фильма "{await db.get_film_name(user_id=callback_query.from_user.id)}"')
            for i in range(len(data)):
                album_builder.add_photo(
                    media=data[i]['url']
                )
            await callback_query.bot.delete_message(chat_id=callback_query.from_user.id,
                                                    message_id=await db.get_message_delete_id(
                                                        user_id=callback_query.from_user.id
                                                    )
                                                    )
            await callback_query.message.answer_media_group(
                media=album_builder.build()
            )


@router.callback_query(F.data == 'sap')
async def handle_info(callback_query: types.CallbackQuery):
    data = await m_func.sap(
        message=await db.get_film_name(
            user_id=callback_query.from_user.id
        )
    )
    if data == 'Нет информации об этом фильме' or data == 'К сожалению нет информации о сиквелах или приквелах к данному фильму':
        action_sender = ChatActionSender(bot=callback_query.message.bot,
                                         chat_id=callback_query.message.chat.id,
                                         interval=1,
                                         action=ChatAction.TYPING)
        async with action_sender:
            try:
                await callback_query.bot.edit_message_media(chat_id=callback_query.message.chat.id,
                                                            message_id=callback_query.message.message_id,
                                                            media=types.InputMediaPhoto(
                                                                media=await db.get_film_pic_id(
                                                                    user_id=callback_query.from_user.id
                                                                ),
                                                                caption=await db.get_film_name_etc(
                                                                    user_id=callback_query.from_user.id
                                                                ) + '\n' + data
                                                            ),
                                                            reply_markup=await info_kb()
                                                            )
            except exceptions.TelegramBadRequest:
                await callback_query.answer()
    else:
        action_sender = ChatActionSender(bot=callback_query.message.bot,
                                         chat_id=callback_query.message.chat.id,
                                         interval=1,
                                         action=ChatAction.UPLOAD_PHOTO)
        async with action_sender:
            album_builder = MediaGroupBuilder(
                caption=f'Сиквелы и приквелы к фильму "{await db.get_film_name(user_id=callback_query.from_user.id)}":\n\n'
                        + '\n'.join(f'{i + 1}. {data[i]["name"]} ({data[i]["relationType"]})' for i in range(len(data))
                                    )
            )
            for i in range(len(data)):
                album_builder.add_photo(
                    media=data[i]['url']
                )
            await callback_query.bot.delete_message(chat_id=callback_query.from_user.id,
                                                    message_id=await db.get_message_delete_id(
                                                        user_id=callback_query.from_user.id
                                                    )
                                                    )
            await callback_query.message.answer_media_group(
                media=album_builder.build()
            )


@router.callback_query(F.data == 'videos')
async def handle_info(callback_query: types.CallbackQuery):
    action_sender = ChatActionSender(bot=callback_query.message.bot,
                                     chat_id=callback_query.message.chat.id,
                                     interval=1,
                                     action=ChatAction.TYPING)
    async with action_sender:
        try:
            await callback_query.answer()
            await callback_query.bot.edit_message_media(chat_id=callback_query.message.chat.id,
                                                        message_id=callback_query.message.message_id,
                                                        media=types.InputMediaPhoto(
                                                            media=await db.get_film_pic_id(
                                                                user_id=callback_query.from_user.id),
                                                            caption=await db.get_film_name_etc(
                                                                user_id=callback_query.from_user.id
                                                            ) + '\n' + await m_func.videos(
                                                                message=await db.get_film_name(
                                                                    user_id=callback_query.from_user.id)
                                                            )),
                                                        reply_markup=await info_kb())
        except exceptions.TelegramBadRequest:
            await callback_query.answer()
