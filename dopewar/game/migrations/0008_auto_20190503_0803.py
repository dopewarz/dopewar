# Generated by Django 2.0.13 on 2019-05-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20190503_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='cash',
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='player',
            name='debt',
            field=models.IntegerField(default=2200),
        ),
        migrations.AlterField(
            model_name='player',
            name='health',
            field=models.IntegerField(default=100),
        ),
    ]
