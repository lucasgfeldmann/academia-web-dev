from django.db.models import Sum, Count, Case, When, IntegerField, DecimalField
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from .models import Pendencia
from django.contrib.auth.decorators import login_required


@login_required
def relatorio(request):
    data = (
        Pendencia.objects.annotate(mes=TruncMonth("data"))
        .values("mes")
        .annotate(
            total=Sum("valor"),
            total_nao=Sum(
                Case(When(compensado=False, then="valor"), output_field=DecimalField())
            ),
            nao_compensados=Count(
                Case(When(compensado=False, then=1), output_field=IntegerField())
            ),
        )
        .order_by("mes")
    )

    context = {"data": data}
    return render(request, "emhaver/relatorio.html", context)
