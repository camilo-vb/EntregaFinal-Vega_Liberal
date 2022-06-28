from django.db import models
from ckeditor.fields import RichTextField
#from ckeditor.fields import RichTextUploadingField
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    country = models.CharField(max_length=20)
    article_content = RichTextField(blank=True, null=True)
    article_description = RichTextField(blank=True, null=True)
    article_date = models.DateField()
    article_author = models.CharField(max_length=20)

    def __str__(self):
        return f'Nombre del Artículo: {self.title} \n País sobre el artículo: {self.country} \n Descripción del artículo: {self.article_description} \n Autor: {self.article_author}'


