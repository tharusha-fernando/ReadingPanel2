# Generated by Django 4.1.6 on 2023-02-14 14:52

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_alter_book_date_alter_chapter_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='book',
            name='User',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 14, 14, 52, 54, 523450, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 14, 14, 52, 54, 524447, tzinfo=datetime.timezone.utc)),
        ),
    ]
