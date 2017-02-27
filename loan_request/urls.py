from django.conf.urls import url, include
from growthstreet.urls import urlpatterns
from loan_request import views

loan_urls = [
    url(r'^test/', views.test)
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(loan_urls))
]