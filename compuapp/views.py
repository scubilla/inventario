from django.shortcuts import render, redirect
from .forms import ComputerForm
from .models import Computer


# Create your views here.
def home(request):
    title = "Bienvenidos, esta es la pagina principal"
    context ={
    "title" : title,
    }
    return render(request, "home.html", context)

def computer_entry(request):
    title = "Agregar equipo"
    form = ComputerForm(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect("/computer_list")

    context = {
    "title": title,
    "form": form,
    }
    return render(request, "add_computer.html",context)

def computer_list(request):
    title = "Lista de Equipos"
    queryset = Computer.objects.all()
    context = {
    "title": title,
    "queryset": queryset,
    }
    return render(request, "list_computer.html",context)


