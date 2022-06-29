from django.urls import path
from article import views
from .views import ArticleDetailView, AddCommentView


urlpatterns = [
    path('article', views.article_list, name='articles'),
    path('article/create', views.article_form, name='article_form'),
    path('article/<int:pk>/update', views.update_article, name='article_update'),
    path('article/<int:pk>/delete', views.delete_article, name='article-delete'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('comment/<int:pk>/delete', views.delete_comment, name='comment-delete'),
    ]