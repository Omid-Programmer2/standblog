# Generated by Django 5.1.2 on 2024-10-19 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_category_alter_article_pub_date_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 19, 21, 3, 17, 630250, tzinfo=datetime.timezone.utc)),
        ),
    ]