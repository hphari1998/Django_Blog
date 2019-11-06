from django.forms import ModelForm

from article.models import Article


class ArticleModelForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'thumbnail','content']
