from .views import relatorio
from django.urls import path

urlpatterns = [

    path('', relatorio),
]
