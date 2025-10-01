from django.db import models
from django.contrib.auth.models import User


class Plano(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Exercicio(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class PlanoExercicio(models.Model):
    plano = models.ForeignKey(Plano, models.PROTECT)
    ordem = models.PositiveIntegerField()
    exercicio = models.ForeignKey(Exercicio, models.PROTECT)

    def __str__(self):
        return f"{self.plano} - {self.ordem}° - {self.exercicio}"


class Registro(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, models.PROTECT)
    serie = models.PositiveIntegerField(default=1)
    carga = models.FloatField()
    repeticoes = models.PositiveIntegerField()
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

    def __str__(self):
        return f"{self.exercicio} - {self.serie}"
    
