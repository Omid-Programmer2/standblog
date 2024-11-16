# Generated by Django 5.1.2 on 2024-11-16 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0049_alter_article_author_alter_article_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/articles'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 16, 16, 21, 56, 360733, tzinfo=datetime.timezone.utc)),
        ),
    ]