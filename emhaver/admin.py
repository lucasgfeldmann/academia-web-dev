from django.contrib import admin
from .models import Cliente, Pendencia


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)


@admin.register(Pendencia)
class PendenciaAdmin(admin.ModelAdmin):
    list_display = ("cliente", "valor", "data", "compensado")
    list_filter = ("compensado", "cliente", "data")
    search_fields = ("cliente__nome",)
    list_editable = ("compensado",)
    date_hierarchy = "data"
