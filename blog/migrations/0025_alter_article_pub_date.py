# Generated by Django 5.1.2 on 2024-10-23 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 23, 18, 7, 2, 12503, tzinfo=datetime.timezone.utc)),
        ),
    ]
