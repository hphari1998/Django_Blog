from django.conf.urls import url

from article.views import list_article

urlpatterns = [
    url(r'^$', list_article),
]

