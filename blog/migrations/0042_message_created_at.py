# Generated by Django 5.1.2 on 2024-11-04 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
