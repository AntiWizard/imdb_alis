# Generated by Django 4.1.3 on 2022-11-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_rename_status_movie_is_valid'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='lol',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
