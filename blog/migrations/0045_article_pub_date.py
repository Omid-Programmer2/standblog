# Generated by Django 5.1.2 on 2024-11-16 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_message_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 16, 7, 57, 42, 454851, tzinfo=datetime.timezone.utc)),
        ),
    ]
