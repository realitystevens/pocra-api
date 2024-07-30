import os
from decouple import config
from django.core.wsgi import get_wsgi_application



if config('ENVIRONMENT') == 'PRODUCTION':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.development')

application = get_wsgi_application()
