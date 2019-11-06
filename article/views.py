from django.shortcuts import render, HttpResponsePermanentRedirect
from article.models import Article

from article.forms import ArticleModelForm

def list_article(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'article/list.html', {'articles': articles})

def view_article(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article/details.html', {'article': article})

def create_article(request):
    if request.method == 'POST':
        article_form = ArticleModelForm(request.POST, request.FILES)
        if article_form.is_valid():
            artcile_obj = article_form.save(commit=False)
            artcile_obj.author = request.user
            artcile_obj.save()
            return HttpResponsePermanentRedirect('/')
    else:
        article_form = ArticleModelForm()
    return render(request, 'article/form.html', {'form': article_form})
