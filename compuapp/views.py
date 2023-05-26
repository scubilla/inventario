from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Bienvenidos, esta es la pagina principal"
    context ={
    "title" : title,
    }
    return render(request, "home.html", context)