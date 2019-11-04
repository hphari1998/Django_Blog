from django.conf.urls import url

from post import views

urlpatterns = [
    url ('$', views.hello, name='index'),
]