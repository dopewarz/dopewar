# Generated by Django 2.0.13 on 2019-05-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='expense',
            field=models.IntegerField(default=0),
        ),
    ]