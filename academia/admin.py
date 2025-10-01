from django.contrib import admin
from .models import Plano, Exercicio, PlanoExercicio, Registro


@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)


@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)


@admin.register(PlanoExercicio)
class PlanoExercicioAdmin(admin.ModelAdmin):
    list_display = ("plano", "ordem", "exercicio")
    list_filter = ("plano", "exercicio")
    search_fields = ("plano__nome", "exercicio__nome")


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "exercicio",
        "serie",
        "carga",
        "repeticoes",
        "inicio",
        "fim",
    )
    list_filter = ("user", "exercicio", "inicio")
    search_fields = ("user__username", "exercicio__nome")
    ordering = ("-inicio",)
