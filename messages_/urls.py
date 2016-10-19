"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^register/', views.register, name='register'),
    url(r'^confirm/', views.confirm, name='confirm'),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^accounts/new_message/', views.new_message, name='new_message'),
    url(r'^accounts/write_message/', views.write_message, name='write_message'),
    url(r'^accounts/inbox/', views.view_inbox, name='inbox'),
    url(r'^accounts/sent/', views.view_sent, name='sent'),
]
