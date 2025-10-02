from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome


class Pendencia(models.Model):
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    compensado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente} - {self.data}"
