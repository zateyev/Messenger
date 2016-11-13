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
    url(r'^confirm/', views.confirm, name='confirm'),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^accounts/new_message/', views.new_message, name='new_message'),
    url(r'^accounts/inbox/', views.view_inbox, name='inbox'),
    url(r'^accounts/sent/', views.view_sent, name='sent'),
    url(r'^accounts/view_favorites/', views.view_favorites, name='view_favorites'),
    url(r'^accounts/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    url(r'^accounts/delete_from_inbox/', views.delete_from_inbox, name='delete_from_inbox'),
    url(r'^accounts/delete_from_sent/', views.delete_from_sent, name='delete_from_sent'),
    url(r'^accounts/delete_from_starred/', views.delete_from_starred, name='delete_from_starred'),
]
