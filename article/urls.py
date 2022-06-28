from django.urls import path
from article import views
from .views import ArticleDetailView


urlpatterns = [
    path('article', views.article_list, name='articles'),
    path('article/create', views.article_form, name='article_form'),
    path('article/<int:pk>/update', views.update_article, name='article_update'),
    path('article/<int:pk>/delete', views.delete_article, name='article-delete'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    ]