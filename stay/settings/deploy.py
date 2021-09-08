
from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#  모바일도 가능하도록 허용 (* : 모든 호스트에게 허용)
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django2',
        'USER': 'django2',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb2',
        'PORT': '3306',
    }
}