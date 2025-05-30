from pymongo import MongoClient

INSTALLED_APPS = [
    'django.contrib.admin',  # Административный интерфейс
    'django.contrib.auth',   # Система аутентификации
    'django.contrib.contenttypes',  # Типы контента
    'django.contrib.sessions',  # Сессии
    'django.contrib.messages',  # Сообщения
    'django.contrib.staticfiles',  # Статические файлы
    'papers',  # Ваше приложение
]

MONGO_CLIENT = MongoClient('localhost', 27017)
MONGO_DB = MONGO_CLIENT['research_papers']
MONGO_COLLECTION = MONGO_DB['papers']

DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'research_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Папки с пользовательскими шаблонами (если есть)
        'APP_DIRS': True,  # Искать шаблоны внутри приложений
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Для работы сессий
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Для аутентификации
    'django.contrib.messages.middleware.MessageMiddleware',  # Для сообщений
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',  # Отключаем стандартную базу данных Django
    }
}

STATIC_URL = '/static/'
SECRET_KEY = 'django-insecure-0se3m9y^q2z@#x!b&k$6l^a5p8w)j7z!v@h2g$#tqf@9o+1e*'