# Generated by Django 4.0.5 on 2022-06-26 20:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
