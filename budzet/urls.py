"""budzet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include,url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from monthly.views import budgetList
from monthly import views
from rest_framework import routers

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^budget/$', views.budgetList.as_view()),
    url(r'^budget/(?P<pk>[0-9]+)/$', views.budgetDetail.as_view()),

url(r'^budget/(?P<pk>[0-9]+)/$', views.budgetDetail.as_view()),
url(r'^due/', include('dueDates.urls')),
url(r'^main/', include('mainBudget.urls')),
url(r'^user/', include('user.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns)