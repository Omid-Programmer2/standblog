# Generated by Django 5.1.2 on 2024-10-19 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_article_author_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text='Enter a valid title', max_length=70, unique=True),
        ),
    ]
