# Generated by Django 3.2.3 on 2021-06-15 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='thumb',
        ),
    ]