# log/urls.py
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from log import views


# We are adding a URL called /home
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='log/home.html'), name='home'),
    url(r'^login/', auth_views.login, {'template_name': 'log/login.html'}, name='login'),
    url(r'^logout/', views.logoutView, name='logout'),
]
