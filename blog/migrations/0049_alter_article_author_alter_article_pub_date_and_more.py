# Generated by Django 5.1.2 on 2024-11-16 16:11

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0048_alter_article_pub_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده مقاله'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 16, 16, 11, 0, 572507, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=70, verbose_name='عنوان'),
        ),
    ]