# Generated by Django 2.2 on 2019-05-08 08:39

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=None),
        ),
    ]
