from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def importe_total_carro(request):
    total=0
    if "carro" in request.session.keys():
        for key ,valor in request.session["carro"].items():
            total +=(float(valor["precio"])*valor["cantidad"])
    return{"importe_total_carro":total}
