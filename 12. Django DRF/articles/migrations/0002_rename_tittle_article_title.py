# Generated by Django 3.2.12 on 2022-04-20 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tittle',
            new_name='title',
        ),
    ]