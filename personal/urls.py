from django.conf.urls import url, include
from personal import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'create/$', views.add_account, name='create'),
    url(r'contact/$', views.contact, name='contact'),
    url(r'chart/data/$', views.ChartData.as_view(), name='chart-data'),
    url(r'select/$',views.select, name='select'),
]
