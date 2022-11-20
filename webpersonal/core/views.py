from django.shortcuts import render, HttpResponse
#HttResponse nos permite constar a una petición devolviendo un código
# Create your views here.


def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    return render(request, "core/contact.html")