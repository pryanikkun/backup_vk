from tools import from_vk_to_ya

if __name__ == '__main__':
    user_id = input('Введите id пользователя: ')
    ya_token = input('Введите токен с Полигона Яндекс.Диска: ')
    count_photos = input('Введите число фото, которые вы хотите сохранить '
                         '(опционально): ')

    try:
        count_photos = int(count_photos)
    except:
        count_photos = 5

    from_vk_to_ya(user_id, ya_token, count_photos)


