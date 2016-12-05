from django.conf.urls import url
from dueDates import views

urlpatterns = [
    url(r'^payment/$', views.dates.as_view()),
    url(r'^payment/(?P<pk>[0-9]+)/$', views.dueDatesDetail.as_view()),
]