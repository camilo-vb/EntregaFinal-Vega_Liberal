from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.urls import reverse_lazy
from article.models import Article, Comment
from article.forms import ArticleForm, CommentForm
from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
import random
import string
from django.views.generic import DetailView, CreateView

# Create your views here.
def article_list(request):
    articles = Article.objects.all()

    context_dict = {
        'articles': articles
    }

    return render(
        request=request,
        context=context_dict,
        template_name="article_list.html"
    )

@login_required
def article_form(request):

    if request.method == 'POST':

        article_form = ArticleForm(request.POST)

        print(article_form)

        if article_form.is_valid():

            data = article_form.cleaned_data

            article = Article (
                title=data['title'], 
                country=data['country'], 
                article_content=data['article_content'],
                article_description=data['article_description'],
                article_date=data['article_date'],
                article_author=data['article_author'],
            )

            article.save()
            articles = Article.objects.all()
            context_dict = {
                'articles': articles
            }

            return render(
                request=request,
                context=context_dict,
                template_name= "article_list.html"
            )
    article_form = ArticleForm(request.POST)
    context_dict = {
        'article_form': article_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='article_form.html'
    )

@login_required
def update_article(request, pk: int):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            data = article_form.cleaned_data
            article.title = data['title']
            article.country = data['country']
            article.article_description = data['article_description']
            article.article_content = data['article_content']
            article.article_date = data['article_date']
            article.article_author = data['article_author']
            article.save()

            articles = Article.objects.all()
            context_dict = {
                'articles': articles
            }
            return render(
                request=request,
                context=context_dict,
                template_name="article_list.html"
            )

    article_form = ArticleForm(model_to_dict(article))
    context_dict = {
        'article': article,
        'article_form': article_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='article_form.html'
    )


@login_required
def delete_article(request, pk: int):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()

        articles = Article.objects.all()
        context_dict = {
            'articles': articles
        }
        return render(
            request=request,
            context=context_dict,
            template_name="article_list.html"
        )

    context_dict = {
        'article': article,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='article_confirm_delete.html'
    )


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_details.html'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('articles')


@login_required
def delete_comment(request, pk: int):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        comment.delete()

        comments = Comment.objects.all()
        context_dict = {
            'comments': comments
        }
        return render(
            request=request,
            context=context_dict,
            template_name="article_list.html"
        )

    context_dict = {
        'comment': comment,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='comment_confirm_delete.html'
    )
