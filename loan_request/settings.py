from growthstreet.settings import *

INSTALLED_APPS += (
    'loan_request.apps.LoanRequestConfig',
    'rest_framework'
)

ROOT_URLCONF = 'loan_request.urls'
