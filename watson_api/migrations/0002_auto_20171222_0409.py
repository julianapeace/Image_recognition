# Generated by Django 2.0 on 2017-12-22 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watson_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picturemodel',
            old_name='pic',
            new_name='image',
        ),
    ]