# Generated by Django 3.2.3 on 2021-06-16 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210615_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
