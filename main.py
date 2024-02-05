from tools import from_vk_to_ya

if __name__ == '__main__':
    user_id = input('Введите id пользователя: ')
    ya_token = input('Введите токен с Полигона Яндекс.Диска: ')
    count_photos = input('Введите число фото, которые вы хотите сохранить '
                         '(опционально): ')
    VK_TOKEN = 'vk1.a.6q7wWLWedRp9AOkmnbwaWJK2HUfrdq7TXHw4wa0fg7pwEzeDfeR4g_7FXTXntrJC5VgjfV_H0TsBlHP93l4c_oA1rknVJWVt1eCiCStBqonFYEGW_EIuXoiU51UxIdu5VpO69jc-1a70vGVurffApSA5jGwS750rLZZgp3DMV1Gi7lSTAJIkKgdBt-ED-nml'

    try:
        count_photos = int(count_photos)
    except:
        count_photos = 5

    from_vk_to_ya(user_id, ya_token, count_photos, VK_TOKEN)


