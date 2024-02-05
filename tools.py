import json
import requests

from classes import VKAPIClient, ProfilePhoto, YandexClient
from conf import VK_TOKEN


def _get_all_likes(photos):
    """ Создает список лайков всех фото """
    likes = []
    for photo in photos:
        likes.append(photo.likes)
    return likes


def make_photos_objects(photos_data):
    """ Получение нужных полей для работы """
    photos_objects = []
    for photo in photos_data:
        like_photo = photo['likes']['count']
        date_photo = photo['date']
        for size in photo['sizes']:
            if size['type'] == 'w':
                size_photo = size['type']
                url_photo = size['url']
            elif size['type'] == 'z':
                size_photo = size['type']
                url_photo = size['url']
        photos_objects.append(ProfilePhoto(like_photo, date_photo,
                                           size_photo, url_photo))
    likes = _get_all_likes(photos_objects)
    for i in photos_objects:
        i.make_photo_names(likes)
    return photos_objects


def photo_to_json(photos):
    """ Создает файл с информацией о загруженных фото """
    list_for_json = []
    for photo in photos:
        list_for_json.append({
            'file_name': photo.file_name,
            'size': photo.size,
        })

    with open('profile_photos.json', 'w') as file:
        json.dump(list_for_json, fp=file, indent=4)


def photo_to_ya(ya, photos):
    """ Загружает фото на Я.Диск """
    folder_name = 'VKAvatars'
    ya.create_folder(folder_name)
    for photo in photos:
        ya.upload_photo(folder_name, photo)


def from_vk_to_ya(vk_user_id, ya_token, count_photos):
    """ Функция, управляющая переходами по функциям """
    # Получаем фото из VK API
    vk = VKAPIClient(VK_TOKEN, vk_user_id)
    photos_data = vk.photo_get(count_photos)

    # Подготовим данные для удобной работы
    photos_objects = make_photos_objects(photos_data['response']['items'])

    # Отправим на Я.Диск
    ya = YandexClient(ya_token)
    photo_to_ya(ya, photos_objects)

    # Запишем информацию в файл
    photo_to_json(photos_objects)

    print('Готово!')
