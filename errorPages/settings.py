"""
Django settings for errorPages project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import pymysql
pymysql.install_as_MySQLdb()



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6jr4wxeimt4qvekgb_8bytg@vtstd72h+7zsokttnf$47qmq@x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'users',
    'productos',
    'categorias',
    'rest_framework',
    'alumnos',
    'rest_framework_simplejwt',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

#constante prohibida:
#permitir la conexion de cualquier origen a la app
CORS_ALLOW_ALL_ORIGINS = True


ROOT_URLCONF = 'errorPages.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'errorPages.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Motor de base de datos
        'NAME': 'bd',           # Nombre de la base de datos
        'USER': 'root',                 # Usuario de la base de datos
        'PASSWORD': 'root',           # Contraseña del usuario
        'HOST': 'localhost',                  # Dirección del servidor de BD
        'PORT': '3306',                       # Puerto de MySQL (por defecto 3306)
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Que va  ahacer Django cuando pase un 404
HANDLER404 = 'app.views.show_error_404'

#Que va  ahacer Django cuando pase un 500
HANDLER500 = 'app.views.show_error_500'

LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/home' # Dónde irán los usuarios tras iniciar sesión
LOGOUT_REDIRECT_URL = '/users/login/'


SEARCH_API_KEY='AIzaSyDgDXqw-LrWKjSs_8HnTVMjYF6RmiWSZUw'
SEARCH_ENGINE_ID='814af8d084c1f4965'


AUTH_USER_MODEL = 'users.CustomUser'

#MIAS
#SEARCH_API_KEY = ''
#SEARCH_ENGINE_ID='b7b6c6e848e004e3d'

REST_FRAMEWORK={
    'DEFAUL_AUTHENTICATION_CLASSES':(
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

AUTH_USER_MODEL= 'users.CustomUser'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#Configuración para Gmail
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# Usar su correo de UTEZ
EMAIL_HOST_USER = "alexisduranduran105@gmail.com"
# Obtener de https://myaccount.google.com/apppasswords
EMAIL_HOST_PASSWORD = "ocyd zpac nkua mzqj"