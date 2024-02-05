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


class ProfilePhoto:
    def __init__(self, like_photo, date_photo, size_photo, url_photo):
        self.file_name = None
        self.likes = like_photo
        self.date_created = date_photo
        self.size = size_photo
        self.url = url_photo

    def make_photo_names(self, likes):
        """ Заполняет имя фото """
        if likes.count(self.likes) == 1:
            self.file_name = f'{self.likes}.jpg'
        else:
            self.file_name = f'{self.likes}_{self.date_created}.jpg'


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

    def upload_photo(self, folder_name, photo):
        """ Функция загружает фото в папку на Я.Диске """
        url_upload_photo = f'{self.YA_BASE_URL}/v1/disk/resources/upload'
        params = {
            'path': f'{folder_name}/{photo.file_name}',
            'url': photo.url,
        }
        response = requests.post(url_upload_photo,
                                 headers=self.headers,
                                 params=params)
