from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^all/$', views.userList.as_view()),
    url(r'^all/(?P<user_name>[0-9]+)/$', views.userDetail.as_view()),
]