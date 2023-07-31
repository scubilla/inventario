from django.shortcuts import render, redirect, get_object_or_404
from .forms import ComputerForm, ComputerSearchForm
from .models import Computer


# Create your views here.
def home(request):
    title = "Bienvenidos, esta es la paginal "
    context ={
    "title" : title,
    }
    return render(request, "home.html", context)

def computer_entry(request):
    title = "Agregar equipo"
    form = ComputerForm(request.POST or None)
    if form.is_valid():
       form.save()
       form.save_m2m()
       return redirect("/computer_list")

    context = {
        "title": title,
        "form": form,
        }
    return render(request, "add_computer.html",context)



def computer_list(request):
    title = "Lista de Equipos"
    queryset = Computer.objects.all()
    form = ComputerSearchForm(request.POST or None)
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
       queryset = Computer.objects.all().order_by('-timestamp').filter(computer_name__icontains=form['computer_name'].value(), users_name__icontains = form['users_name'].value())
       context = {
            "title": title,
            "queryset": queryset,
            "form": form,
        }
    return render(request, "list_computer.html",context)


def computer_edit(request, id=None):
    instance = get_object_or_404(Computer, id=id)
    form = ComputerForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        return redirect('/computer_list')
    context = {
        "title": 'Editando ' + str(instance.computer_name),
        "instance": instance,
        "form": form,
        }
    return render(request, "add_computer.html", context)

def computer_delete(request, id=None):
    instance = get_object_or_404(Computer, id=id)
    instance.delete()
    return redirect('/computer_list')

def computer_list(request):
    title = "Lista de Equipos"
    queryset = Computer.objects.all()

    context = {
    "title": title,
    "queryset": queryset,
    }
    return render(request, "list_computer.html",context)


