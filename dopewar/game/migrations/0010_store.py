# Generated by Django 2.1.7 on 2019-05-11 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_player_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField(default=25)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.country')),
            ],
        ),
    ]