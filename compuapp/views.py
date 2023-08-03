from django.shortcuts import render, redirect, get_object_or_404
from .forms import ComputerForm, ComputerSearchForm, OperatingSystemForm
from .models import Computer, ComputerHistory
from django.http import HttpResponse
import csv
from django.contrib import messages


# Create your views here.
def home(request):
    title = "Bienvenidos, esta es la paginal "
    context ={
    "title" : title,
    }
    return render(request, "base.html", context)

def computer_entry(request):
    title = "Agregar equipo"
    form = ComputerForm(request.POST or None)
    if form.is_valid():
       form.save()
       form.save_m2m()
       messages.success(request, 'Los datos del equipo han sido guardados exitosamente.')
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
       if form['export_to_CSV'].value() == True:
           response = HttpResponse(content_type='text/csv')
           response['Content-Disposition'] = 'attachment; filename="Computer list.csv"'
           writer = csv.writer(response)
           writer.writerow(['COMPUTER NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE','TIMESTAMP'])
           instance = queryset
           for row in instance:
               writer.writerow(
                   [row.computer_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name,row.location, row.purchase_date, row.timestamp])
           return response

    return render(request, "list_computer.html",context)


def computer_edit(request, id=None):
    instance = get_object_or_404(Computer, id=id)
    form = ComputerForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Los datos del equipo han sido guardados exitosamente.')
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


def computerhistory_list(request):
    title = 'Historico Movimiento de Equipos'
    queryset = ComputerHistory.objects.all()
    context = {
       "title": title,
       "queryset": queryset,
    }
    return render(request, "computerhistory_list.html",context)

def settings(request):
    title = 'Agregar Sistema Operativo'
    form = OperatingSystemForm(request.POST or None)
    if form.is_valid():
       form.save()
       messages.success(request, 'Los datos han sido guardados satisfactoriamente.')
       return redirect('/computer_list')
    context = {
              "title": title,
              "form": form,
    }
    return render(request, "settings.html",context)

