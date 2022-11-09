from django.shortcuts import render, HttpResponse
#HttResponse nos permite constar a una petición devolviendo un código
# Create your views here.

def home(request):
    html_response = "<h1>Mi Web Personal</h1>"
    for i in range(10):
        html_response += "<p>Esto es la portada</p>"
    return HttpResponse(html_response)

