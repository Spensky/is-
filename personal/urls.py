from django.conf.urls import url, include
from  personal import views

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
]
