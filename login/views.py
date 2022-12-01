from ast import Return
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import is_valid_path
from .models import login_1
from.forms import formulariocadastro



def login (request):
    tela = login_1.objects.all()
    return render (request, "html/base_login.html", {'cliente':tela})


def cadastro (request):
    form = formulariocadastro(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('pagina_inicial')

    return render(request,"html/cadastro.html", {'login':form})
    

    
    




    
    
    

    
    