from project.settings.main import *
import cloudinary
import cloudinary.api
import cloudinary.uploader
import dj_database_url



DEBUG = True

INSTALLED_APPS = [
    *INSTALLED_APPS[:6],
    'cloudinary',
    'cloudinary_storage',
    *INSTALLED_APPS[6:]
]


DATABASES = {
    'default':dj_database_url.parse(os.getenv("DATABASE_URL") or config('DATABASE_URL'))
}


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUDNAME'),
    'API_KEY': config('CLOUDINARY_APIKEY'),
    'API_SECRET': config('CLOUDINARY_APISECRET'),
}

cloudinary.config(
    cloud_name = CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key = CLOUDINARY_STORAGE['API_KEY'],
    api_secret = CLOUDINARY_STORAGE['API_SECRET'],
)
