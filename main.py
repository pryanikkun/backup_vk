import logging
from tools import from_vk_to_ya

if __name__ == '__main__':
    logging.basicConfig(filename="basic.log", level=logging.DEBUG)
    user_id = input('Введите id пользователя: ')
    ya_token = input('Введите токен с Полигона Яндекс.Диска: ')
    count_photos = input('Введите число фото, которые вы хотите сохранить '
                         '(опционально): ')
    VK_TOKEN = ''  # место для токена, полученного с помощью get_token.py

    try:
        count_photos = int(count_photos)
    except:
        count_photos = 5

    from_vk_to_ya(user_id, ya_token, count_photos, VK_TOKEN)


