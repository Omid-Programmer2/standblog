# Generated by Django 5.1.2 on 2024-11-05 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0043_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
