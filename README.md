# Blog

***Приложение для ведения блога***

Создание публикаций только через [админ панель](http://127.0.0.1:8000/admin)

В админ панели можно создавать посты, указывать теги. Тело поста задается в разметке Markdown. Тип поста:
* Draft - черновик
* Published - готов к публикации

[Главная страница](http://127.0.0.1:8000/blog)

Осуществлен [поиск постов](http://127.0.0.1:8000/search) (приоритет отделается словам в названии статьи)

Также возможет поиск по тегу, по нажатии по нему

При открытии статьи, можно увидеть комментарии, добавить свой комментарий.


# Запуск приложения

1. Клонирование репозитория

`https://github.com/OksanaZakharovaIP-31/Blog.git`

2. Установка виртуального окружения и его активация

`python -m venv venv`

`venv\Scripts\activate.bat` - Windows

`source venv/bin/activate` - Linux and MacOS

3. Установка зависимостей

`pip install -r requirements.txt`

4. База данных - PostgreSQL. можно использовать любоую соглаcно [документации](https://docs.djangoproject.com/en/4.2/ref/databases/)
5. Все ключи, пароли храняться в файле .env (создать в папке проекта) (заполнить для себя)

```
SECRET_KEY=
DEBUG=
NAME_DB=
USER_DB=
PASSWORD_DB=
HOST_DB=
POST=
```

6. Запуск миграций
```
python namage.py makemigrations
python manage.py migrate
```

7. Запуск проекта

`python manage.py runserver`

8. Создание суперпользователя

`python manage.py createsuperuser`

Далее следовать указаниям в терминале
