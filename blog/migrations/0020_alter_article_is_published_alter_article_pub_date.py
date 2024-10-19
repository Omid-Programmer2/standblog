# Generated by Django 5.1.2 on 2024-10-19 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_article_is_published_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 19, 16, 5, 35, 314460, tzinfo=datetime.timezone.utc)),
        ),
    ]