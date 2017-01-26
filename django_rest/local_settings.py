
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_rest',
        'USER': 'django_rest',
        'PASSWORD': '123rest',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
