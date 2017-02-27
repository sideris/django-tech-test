from growthstreet.settings import *

INSTALLED_APPS += (
    'loan_request.apps.LoanRequestConfig',
    'rest_framework'
)

ROOT_URLCONF = 'loan_request.urls'

DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'loan',
        'USER': 'petros',
        'PASSWORD': 'supersecret',
        'HOST': 'postgres',
        'PORT': '5432',
}
