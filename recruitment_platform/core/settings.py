# settings.py

import os
from pathlib import Path


# Configuration de la base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'recruitment_db',  
        'USER': 'postgres',       
        'PASSWORD': 'reda23',     
        'HOST': 'localhost',       
        'PORT': '5432',          
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware pour l'authentification
    'django.contrib.messages.middleware.MessageMiddleware',  # Middleware pour les messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Le backend pour utiliser les templates Django
        'DIRS': [
            # Ajoutez ici le répertoire où vous stockez vos templates personnalisés
        ],
        'APP_DIRS': True,  # Si vous souhaitez que Django cherche des templates dans vos applications
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',  # Requis pour l'authentification
                'django.contrib.messages.context_processors.messages',  # Requis pour les messages
            ],
        },
    },
]



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  
]
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
ROOT_URLCONF = 'recruitment_platform.urls'
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'core.exceptions.custom_exception_handler',
}




