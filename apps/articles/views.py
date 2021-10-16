from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ["photo","title", "summary", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ["photo","title", "summary", "body"]

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('myarticle_list')

class MyArticleListView(LoginRequiredMixin, ListView):
    template_name = 'myarticle_list.html'

    def get_queryset(self):
        self.author_name = get_object_or_404(User, username=self.request.user)
        return Article.objects.filter(author=self.author_name)

