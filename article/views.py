from django.shortcuts import render
from article.models import Article

def list_article(request):
    articles = Article.objects.all()
    return render(request, 'article/list.html', {'articles': articles})