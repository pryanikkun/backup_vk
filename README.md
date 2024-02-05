# Резервное копирование
___
### Входные данные:
Пользователь вводит:
- id пользователя vk;
- токен с Полигона Яндекс.Диска;
- количество резервируемых фото (опционально).

### Выходные данные:
- json-файл с информацией по файлу:
- Измененный Я.диск, куда добавились фотографии.
___
### Файл get_token.py
Не связан с работой основной программы. Нужен для получения токена. Выводит url для получения токена.

### Файл main.py
Запускает работу программы.

### Файл classes.py
В этом файле хранятся классы для работы с VK, Я.диск, а также для работы с данными о фотографиях.

### Файл tools.py
В этом файле хранятся функции, реализующие логику программы по частям (для каждой функции создана краткая документация).

### Файл basic.log
Содержит описание всех событий работы программы.






