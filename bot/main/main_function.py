import aiohttp
import asyncio
from settings import HEADERS, RELATION_TYPES
from aiogram.utils.formatting import Text, Bold


# Film id in kinopoisk
async def film_id(message):
    async with aiohttp.ClientSession() as session:
        url = f'https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={message}'
        async with session.get(url, headers=HEADERS) as request:
            response = await request.json()
            films = response.get('films', [])
            return films[0]['filmId'] if films else False


# Film full info
async def ffi(message):
    filmId = await film_id(message)
    if not filmId:
        return False

    async with aiohttp.ClientSession() as session:
        url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{filmId}'
        async with session.get(url, headers=HEADERS) as request:
            return await request.json()


# Necessary information about films
async def nec_info(message):
    data = await ffi(message)
    if not data:
        return 1
    else:
        try:
            name = f'{data.get("nameRu")} - {data.get("nameOriginal")}' if data.get("nameOriginal") else data.get("nameRu")
            country = data.get("countries")[0]["country"] if data.get("countries") else None
            length = data.get("filmLength") if data.get("filmLength") else None
            poster_url = data.get("posterUrl")
            age_limits = data.get("ratingAgeLimits")[3:] if data.get("ratingAgeLimits") else None
            kinopoisk = data.get("ratingKinopoisk") if data.get("ratingKinopoisk") else None
            imdb = data.get("ratingImdb") if data.get("ratingImdb") else None
            genres = data.get("genres") if data.get("genres") != [] else None
            short_desc = data.get("shortDescription") if data.get("shortDescription") else None
            ratings = []

            if kinopoisk is not None:
                ratings.append({"rate": f'Кинопоиск: {kinopoisk}/10'})
            if imdb is not None:
                ratings.append({"rate": f'IMDB: {imdb}/10'})

            info = {
                "film_id": data.get("kinopoiskId"),
                "name": name,
                "country": country,
                "year": data.get("year"),
                "length": length,
                "poster_url": poster_url,
                "age_limits": age_limits,
                "ratings": ratings,
                "genres": genres,
                "film_or_serial": data.get("serial"),
                "short_description": short_desc,
                "description": data.get("description"),
            }
            return info

        except:
            return 2


# Information about the film's budget and box office receipts
async def money(message):
    filmId = await film_id(message)
    if not filmId:
        return 'Нет информации об этом фильме'

    async with aiohttp.ClientSession() as session:
        url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{filmId}/box_office'
        async with session.get(url, headers=HEADERS) as request:
            res = await request.json()
    if res['total'] == 0:
        return 'Нет информации о бюджете и сборах для этого фильма'
    budget = ''
    text = 'Кассовые сборы:\n'
    items = res["items"]

    async def fetch_data(item):
        nonlocal text
        if item["type"] == 'BUDGET':
            nonlocal budget
            budget = f'Бюджет фильма: {item["amount"]:,}'.replace(",", " ") + ' $\n'
        else:
            amount = f'{item["amount"]:,}'.replace(",", " ")
            locations = {"RUS": "В России", "USA": "В США", "WORLD": "В мире"}
            text += f'· {locations.get(item["type"], "Другие страны")} {amount} $\n'

    await asyncio.gather(*[fetch_data(item) for item in items])

    return budget + text if len(text) > 17 else budget


# Information about the film's awards
async def awards(message):
    filmId = await film_id(message)
    if not filmId:
        return 'Нет информации об этом фильме'

    async with aiohttp.ClientSession() as session:
        url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{filmId}/awards'
        async with session.get(url, headers=HEADERS) as request:
            res = await request.json()

    text = res['items']
    result = 'Список наград:\n'
    result += '\n'.join(f'• Победил в {award["nominationName"]} в {award["year"]} году'
                        for award in text if award.get('win') and not award.get("persons"))

    return result if len(result) > 18 else 'У данного фильма нет наград'


# Related films
async def similar_movies(message):
    filmId = await film_id(message)
    if not filmId:
        return 'Нет информации об этом фильме'

    async with aiohttp.ClientSession() as session:
        url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{filmId}/similars'
        async with session.get(url, headers=HEADERS) as request:
            res = await request.json()

    if 'items' not in res or not res['items']:
        return 'Похожих фильмов не найдено'

    data = {}
    for i, item in enumerate(res['items'][:10]):
        name_ru = item.get("nameRu")
        name_original = item.get("nameOriginal")
        name = f'{name_ru} - {name_original}' if name_original else name_ru
        film_pic = item.get("posterUrlPreview", "")
        data[i] = {'name': name, 'url': film_pic}

    return data


# Images related to the film
async def images(message):
    filmId = await film_id(message)
    if not filmId:
        return 'Нет информации об этом фильме'

    async with aiohttp.ClientSession() as session:
        url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{filmId}/images'
        async with session.get(url, headers=HEADERS) as request:
            res = await request.json()
    if res["items"][0]["imageUrl"] == '':
        return 'К сожалению нет информации о фото к данному фильму'

    data = {}
    k = min(res['total'], 10)
    for i, item in enumerate(res['items'][:k]):
        film_pic = item.get("imageUrl", "")
        data[i] = {'url': film_pic}

    return data


# Sequels and prequels
async def sap(message):
    filmId = await film_id(message)
    if not filmId:
        return 'Нет информации об этом фильме'

    async with aiohttp.ClientSession() as session:
        url = f'https://kinopoiskapiunofficial.tech/api/v2.1/films/{filmId}/sequels_and_prequels'
        async with session.get(url, headers=HEADERS) as request:
            res = await request.json()
    if not res:
        return 'К сожалению нет информации о сиквелах или приквелах к данному фильму'

    data = {}
    for i, item in enumerate(res[:10]):
        name_ru = item.get("nameRu")
        name_original = item.get("nameOriginal")
        name = f'{name_ru} - {name_original}' if name_original else name_ru
        film_pic = item.get("posterUrlPreview", "")
        relation_type = RELATION_TYPES.get(item.get("relationType"), "")
        data[i] = {'name': name, 'url': film_pic, 'relationType': relation_type}

    return data


# Trailer information for the film
async def videos(message):
    filmId = await film_id(message)
    if filmId is None:
        return 'Нет информации об этом фильме'

    async with aiohttp.ClientSession() as session:
        url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{filmId}/videos'
        async with session.get(url, headers=HEADERS) as request:
            res = await request.json()

    all_trailers = res.get('items', [])
    trailers = [trailer for trailer in all_trailers if trailer.get('site') == 'YOUTUBE' and 'трейлер' in trailer.get('name', '').lower()]

    if not trailers:
        return 'Нет информации о трейлерах для этого фильма'

    trailer_list = '\n'.join(f'• {trailer["name"]} - {trailer["url"]}' for trailer in trailers)
    return 'Список доступных трейлеров:\n' + trailer_list
