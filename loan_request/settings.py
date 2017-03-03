from growthstreet.settings import *

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'loan_request.apps.LoanRequestConfig',
    'rest_framework'
)

APPEND_SLASH = False

ROOT_URLCONF = 'loan_request.urls'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "media")
]
# disable for dev, uncomment if you want to use docker
# DATABASES['default'] = {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'loan',
#         'USER': 'petros',
#         'PASSWORD': 'supersecret',
#         'HOST': 'postgres',
#         'PORT': '5432',
# }
