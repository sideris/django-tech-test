from django.conf.urls import url, include
from growthstreet.urls import urlpatterns
from loan_request import views
from loan_request.views import LoanRequestView

loan_urls = [
    url(r'^test/', views.test),
    url(r'^loan/', views.create_loan_request)
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(loan_urls)),
    url(r'^$', LoanRequestView.as_view(), name='loan_request_view')
]