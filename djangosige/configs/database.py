import os

from django.conf import settings

from djangosige.configs import dj_database_url

engines = {
    'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
}


def config():
    url = os.getenv('DATABASE_URL', '') # 'postgres://vfkemsrlcdwsgz:2f04c320d5e00239ab842d69f2b16bc6bc91c55019939b299d14a13bfed00307@ec2-50-19-224-165.compute-1.amazonaws.com:5432/d88p1mohb28tjh'
    if url != "" and not url is None :
        try:
            print("sigeurl"+url)
            print(dj_database_url.parse(url, ssl_require=True))
        except:
            pass
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
