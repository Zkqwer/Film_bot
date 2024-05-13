from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from database import db


async def url_info_kb(message) -> InlineKeyboardMarkup:
    info_btn = [InlineKeyboardButton(text='Информация', callback_data='info')]
    url = f'https://www.sspoisk.ru/film/{await db.get_film_id(user_id=message.from_user.id)}'
    url_btn = [InlineKeyboardButton(text='Смотреть', url=url)]
    buttons = [info_btn,
               url_btn]
    ikb = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=1)
    return ikb


async def info_kb() -> InlineKeyboardMarkup:
    bdt_btn = InlineKeyboardButton(text='Бюджет и сборы', callback_data='money')
    aws_btn = InlineKeyboardButton(text='Награды', callback_data='awards')
    smr_btn = InlineKeyboardButton(text='Похожие фильмы', callback_data='similar_films')
    img_btn = InlineKeyboardButton(text='Картинки', callback_data='pics')
    sap_btn = InlineKeyboardButton(text='Сиквелы и приквелы', callback_data='sap')
    vid_btn = InlineKeyboardButton(text='Трейлеры', callback_data='videos')
    back_btn = [InlineKeyboardButton(text='Назад', callback_data='back')]
    buttons = [
        [bdt_btn, aws_btn],
        [smr_btn, vid_btn],
        [sap_btn, img_btn],
        back_btn
    ]
    ikb = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=1)
    return ikb
