from django.shortcuts import render
from django.views.generic import (
    CreateView
)
from .forms import ArticleForm
from .models import Article
# Create your views here.

class ArticleCreateView(CreateView):
    template_name = "article/article_create.html"
    form_class = ArticleForm
    queryset = Article.objects.all()