import requests


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

    def photo_get(self, count_photos):
        """ Получает данные о фотографиях """
        params = {
            'owner_id': self.id,
            'album_id': 'profile',
            'rev': 1,
            'extended': 1,
            'photo_sizes': 1,
            'count': count_photos,
        }

        response = requests.get(self.API_BASE_URL + 'photos.get',
                                params={**self.params, **params})
        return response.json()


class YandexClient:
    YA_BASE_URL = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.token = token
        self.headers = {
            'Authorization': f'OAuth {token}'
        }

    def create_folder(self, folder_name):
        """ Функция создает папку VKAvatars на Я.Диске """
        url_create_folder = f'{self.YA_BASE_URL}/v1/disk/resources'
        params = {
            'path': folder_name
        }
        response = requests.put(url_create_folder,
                                headers=self.headers,
                                params=params)

    def upload_photo(self, folder_name, file_name, photo_url):
        """ Функция загружает фото в папку на Я.Диске """
        url_upload_photo = f'{self.YA_BASE_URL}/v1/disk/resources/upload'
        params = {
            'path': f'{folder_name}/{file_name}',
            'url': photo_url,
        }
        response = requests.post(url_upload_photo,
                                 headers=self.headers,
                                 params=params)
