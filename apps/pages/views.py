from django.db import models
from ..articles.models import Article
from django.views.generic import ListView

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'


