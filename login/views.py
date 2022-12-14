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
    
def edit_user(request,pessoa_pk):
    pessoa = login_1.objects.get(pk=pessoa_pk)

    form_2= formulariocadastro(request.POST or None, instance=pessoa)

    if request.POST:
        if form_2.is_valid():
            form_2.save()
            return redirect ('pagina_inicial')

    return render (request, "html/Editar.html", {'login':form_2})


def excluir_user(request, pessoa_pk):
    pessoa = login_1.objects.get(pk=pessoa_pk)
    pessoa.delete()

    return redirect('pagina_inicial')




    
    
    

    
    