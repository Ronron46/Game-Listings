from django.db import models

# Create your models here.

class Plateform(models.Model):
    name=models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

class Game(models.Model):
    title=models.fields.CharField(max_length=100)
    genre=models.fields.CharField(max_length=100)
    annee_de_sortie=models.fields.IntegerField()
    developpeur=models.fields.CharField(max_length=100)
    plateforme=models.ManyToManyField(Plateform)
    def __str__(self):
        return f'{self.title}'

