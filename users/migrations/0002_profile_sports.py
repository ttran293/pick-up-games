# Generated by Django 3.2.8 on 2021-11-04 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sports',
            field=models.TextField(default='No Sports Played'),
        ),
    ]