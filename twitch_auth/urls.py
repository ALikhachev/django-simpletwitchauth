from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login_twitch'),
    url(r'^callback/$', views.callback, name='callback_twitch'),
    url(r'^logout/$', views.logout, name='logout'),
]
