from django.conf.urls import url
from django.contrib import admin
from django.urls import path

# URL Conf
from emp import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    url(r'^emp/list/$', views.list_, name='list'),
    url(r'^emp/(\d{1,3})/$', views.details, name='details'),
    url(r'^emp/(\d{1,3})/delete/$', views.delete, name='delete'),
    url(r'^emp/update/$', views.update, name='update'),

]
