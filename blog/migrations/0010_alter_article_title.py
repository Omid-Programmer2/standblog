# Generated by Django 5.1.2 on 2024-10-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(choices=[('A', 'پایتون'), ('B', 'جنگو')], default='A', max_length=70),
        ),
    ]
