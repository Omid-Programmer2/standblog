# Generated by Django 5.1.2 on 2024-10-23 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_article_status_alter_article_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='status',
            new_name='published',
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 23, 20, 6, 3, 63458, tzinfo=datetime.timezone.utc)),
        ),
    ]
