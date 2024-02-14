import json
import requests

from classes import VKAPIClient, YandexClient


def make_photos(photos_data):
    photos = {}
    for photo in photos_data:
        file_name = f"{photo['likes']['count']}.jpg"
        if file_name in photos.keys():
            file_name = f"{photo['likes']['count']}_{photo['date']}.jpg"

        max_photo = sorted(photo['sizes'],
                           key=lambda size: size['height'] * size['width'],
                           reverse=True)[0]
        size_photo = max_photo['type']
        url_photo = max_photo['url']
        photos[file_name] = {
            "size": size_photo,
            "url": url_photo
        }
    return photos


def photo_to_json(photos):
    """ Создает файл с информацией о загруженных фото """
    list_for_json = []
    for file_name, photo in photos.items():
        list_for_json.append({
            'file_name': file_name,
            'size': photo['size'],
        })

    with open('profile_photos.json', 'w') as file:
        json.dump(list_for_json, fp=file, indent=4)


def photo_to_ya(ya, photos):
    """ Загружает фото на Я.Диск """
    folder_name = 'VKAvatars'
    ya.create_folder(folder_name)
    for file_name, photo in photos.items():
        ya.upload_photo(folder_name, file_name, photo['url'])


def from_vk_to_ya(vk_user_id, ya_token, count_photos, VK_TOKEN):
    """ Функция, управляющая переходами по функциям """
    # Получаем фото из VK API
    vk = VKAPIClient(VK_TOKEN, vk_user_id)
    photos_data = vk.photo_get(count_photos)

    # Подготовим данные для удобной работы
    photos = make_photos(photos_data['response']['items'])

    # Отправим на Я.Диск
    ya = YandexClient(ya_token)
    photo_to_ya(ya, photos)

    # Запишем информацию в файл
    photo_to_json(photos)
