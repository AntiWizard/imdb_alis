# Generated by Django 4.1.3 on 2022-11-15 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_alter_comment_description_alter_comment_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='description',
            new_name='comment_text',
        ),
    ]
