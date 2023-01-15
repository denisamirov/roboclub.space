## Команды для запуска отладочного сервера под Windows
------------------------------------------------------
#### В корне проекта
#### 1. venv\Scripts\activate       Linux Ubuntu: source venv/bin/activate
#### 2. cd public_html\school_section
#### 3. python manage.py runserver


## Команды для обновления статических файлов
------------------------------------------------------
#### В public_html\
#### 1. python school_section\manage.py collectstatic


## Команды для выполнения миграций
-----------------------------------------------------
#### 1. venv\Scripts\activate       Linux Ubuntu: source venv/bin/activate
#### 2. cd public_html\school_section
#### 3. python manage.py makemigrations
#### 3. python manage.py migrate

