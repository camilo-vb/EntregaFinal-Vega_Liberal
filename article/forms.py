from xml.etree.ElementTree import Comment
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Comment

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=40, label='Título')
    country = forms.CharField(max_length=20, label='País')
    article_description = forms.CharField(widget=CKEditorWidget())
    article_content = forms.CharField(widget=CKEditorWidget())
    article_date = forms.DateField()
    article_author = forms.CharField(max_length=20, label='Nombre del autor')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }