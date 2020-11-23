from django.shortcuts import render, redirect
from .forms import NotasForm
from .models import Notas
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.

def index(request):
    listaNotas = Notas.objects.all()
    form = NotasForm()
    contexto = {
        "Notas":listaNotas,
        "notas":form,
    }
    return render(request, "index.html", contexto)

def crear(request):
    if request.method == "POST":
        form = NotasForm(request.POST, request.FILES)
        if form.is_valid():
            notas = form.save(commit=False)
            notas.save()
            return HttpResponse("TAREA CREADO")
        else:
            print(form.errors)

    form = NotasForm()
    return JsonResponse({'Notas':form})

def cargar(request, id):
    notas = Notas.objects.get(pk=id)
    return JsonResponse({'Notas':notas})