from django.shortcuts import render
from .forms import ComputerForm


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
    context = {
    "title": title,
    "form": form,
    }
    return render(request, "add_computer.html",context)

