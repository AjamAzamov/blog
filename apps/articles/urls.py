from django.urls import path
from .views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, MyArticleListView, ArticleUpdateView

urlpatterns = [
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('', MyArticleListView.as_view(), name='myarticle_list')
]