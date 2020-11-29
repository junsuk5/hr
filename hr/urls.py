from django.conf.urls import url
from django.contrib import admin
from django.urls import path

# URL Conf
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    url(r'^emp/list$', views.list_, name='list'),
]
