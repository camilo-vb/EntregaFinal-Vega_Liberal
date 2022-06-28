from django.shortcuts import render
from article.models import Article
from article.forms import ArticleForm
from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
import random
import string
from django.views.generic import DetailView

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

