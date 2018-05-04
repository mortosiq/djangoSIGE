import os

from django.conf import settings
import dj_database_url

engines = {
    'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
}


def config():
    url = os.getenv('DATABASE_URL', '')
    if url != "" and not url is None :
        return dj_database_url.parse(url, ssl_require=True)
    else:

        service_name = os.getenv('DATABASE_SERVICE_NAME', '').upper().replace('-', '_')
        if service_name:
            engine = engines.get(os.getenv('DATABASE_ENGINE'), engines['sqlite'])
        else:
            engine = engines['sqlite']
        name = os.getenv('DATABASE_NAME')
        if not name and engine == engines['sqlite']:
            name = os.path.join(settings.BASE_DIR, 'db.sqlite3')
        return {
            'ENGINE': engine,
            'NAME': name,
            'USER': os.getenv('DATABASE_USER'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD'),
            'HOST': os.getenv('{}_SERVICE_HOST'.format(service_name)),
            'PORT': os.getenv('{}_SERVICE_PORT'.format(service_name)),
        }
