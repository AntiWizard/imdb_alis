# Generated by Django 4.1.3 on 2022-11-23 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviecomment_crewcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crewcomment',
            options={'ordering': ['-created_time']},
        ),
        migrations.AlterModelOptions(
            name='moviecomment',
            options={'ordering': ['-created_time']},
        ),
    ]