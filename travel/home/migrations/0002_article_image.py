# Generated by Django 2.2 on 2019-05-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='article/'),
        ),
    ]
