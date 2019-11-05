from django.contrib import admin

# Register your models here.

from article import models

class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('author__username',)
    list_display = ('title', 'author')

admin.site.register(models.Article, ArticleAdmin)
