# Generated by Django 5.0.6 on 2024-05-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='année_de_sortie',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='développeur',
            field=models.CharField(default='Larian Studio', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.CharField(default='RPG', max_length=100),
            preserve_default=False,
        ),
    ]
