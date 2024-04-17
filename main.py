from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_API, KINOPOISK_API
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.search_by_keyword_request import SearchByKeywordRequest
from kinopoisk_unofficial.request.films.film_request import FilmRequest

bot = Bot(token=TELEGRAM_API)
dp = Dispatcher(bot)
api_client = KinopoiskApiClient(KINOPOISK_API)


async def on_startup(_):
    print('bot start successfully')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        text=f'Привет, {message.from_user.first_name}, я бот который отправит тебе ссылку на бесплатный '
             f'просмотр фильма\n\nЧтобы получить ссылку на фильм - отправь мне его полное название\n\nЕсли что-то не '
             f'получается - /help')


@dp.message_handler(commands=['help'])
async def send_help(message):
    await message.answer(
        text='Здесь рассмотренны возможные проблемы:\n\n• Если вы не можете найти нужный вам '
             'фильм - либо его нет, либо он еще не вышел\n• Если на сайте не открывается '
             'фильм - возможно такого фильма нет в базе, либо он еще не вышел\n')


async def film_info(message):
    film_id = api_client.films.send_search_by_keyword_request(SearchByKeywordRequest(message.text)).films[0].film_id
    data = api_client.films.send_film_request(FilmRequest(film_id)).film
    inline_keyboard = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Смотреть фильм',
                                                                                 url=f'https://www.SSpoisk.ru/film/{data.kinopoisk_id}'))
    if data.serial:
        length = f'Длина серии: {data.film_length} мин'
    else:
        length = f'Длина фильма: {data.film_length} мин'
    await message.answer_photo(photo=data.poster_url_preview,
                               caption=f'<b>{data.name_ru} - {data.name_original} {data.rating_age_limits[3::]}+ ({data.countries[0].country})</b>\n'
                                       f'• Дата выхода: {data.year}\n'
                                       f'• {length}\n'
                                       f'• Рейтинги:\n   '
                                       f'Кинопоиск {data.rating_kinopoisk}/10\n   '
                                       f'IMDB {data.rating_imdb}/10\n'
                                       f'• Описание: {data.short_description}',
                               parse_mode="HTML",
                               reply_markup=inline_keyboard)


@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    try:
        await film_info(message)
    except IndexError:
        await message.answer(text='К сожалению, я не знаю такого фильма')


if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
