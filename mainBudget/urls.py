from django.conf.urls import url
from dueDates import views

urlpatterns = [
    url(r'^budget/$', views.dates.as_view()),
    url(r'^budget/(?P<pk>[0-9]+)/$', views.dueDatesDetail.as_view()),
]