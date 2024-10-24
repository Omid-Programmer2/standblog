# Generated by Django 5.1.2 on 2024-10-24 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_alter_article_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 24, 12, 36, 34, 610103, tzinfo=datetime.timezone.utc)),
        ),
    ]