from django.shortcuts import render, HttpResponse
#HttResponse nos permite constar a una petición devolviendo un código
# Create your views here.

def home(request):
    return HttpResponse("<h1>Mi Web Personal</h1><h2>Portada</h2>")

