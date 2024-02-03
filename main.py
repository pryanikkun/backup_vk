import json

import requests
from conf import VK_TOKEN


class VKAPIClient:
    API_BASE_URL = 'https://api.vk.com/method/'

    def __init__(self, access_token, user_id, version='5.199'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version,
        }

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def photo_get(self):
        params = {
            'owner_id': self.id,
            'album_id': 'profile',
            'rev': 1,
            'extended': 1,
            'photo_sizes': 1,
            'count': 5,
        }

        response = requests.get(self.API_BASE_URL + 'photos.get',
                                params={**self.params, **params})
        return response.json()


def photos_to_json(photos):
    list_of_photo = []
    likes = []
    for photo in photos:
        like_photo = photo['likes']['count']
        date_photo = photo['date']
        if like_photo not in likes:
            list_of_photo.append({
                'file_name': f'{like_photo}.jpg',
                'size': 'z'
            })
        else:
            list_of_photo.append({
                'file_name': f'{like_photo}_{date_photo}.jpg',
                'size': 'z'
            })
        likes.append(like_photo)
    with open('profile_photos.json', 'w') as file:
        json.dump(list_of_photo, fp=file, indent=4)





def from_vk_to_ya(vk_user_id, ya_token, count_photos):
    vk = VKAPIClient(VK_TOKEN, user_id)
    photos_data = vk.photo_get()
    photos_to_json(photos_data['response']['items'])



if __name__ == '__main__':
    # user_id = input('Введите id пользователя: ')
    user_id = '81921805'
    # ya_token = input('Введите токен с Полигона Яндекс.Диска: ')
    ya_token = ''
    # count_photos = input('Введите число фото, которые вы хотите сохранить '
    #                      '(опционально): ')
    count_photos = ''
    try:
        count_photos = int(count_photos)
    except:
        count_photos = 5
    from_vk_to_ya(user_id, ya_token, count_photos)


