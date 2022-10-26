from django.http import HttpResponse
from django.shortcuts import render
from .models import login_1

def login (request):
    tela = login_1.objects.all()

    return render (request, "html/base_login.html", {'cliente':tela})




    
    