from django.shortcuts import render, HttpResponse
#HttResponse nos permite constar a una petición devolviendo un código
# Create your views here.
html_base = """
    <h1>Mi Web Personal</h1>
    <ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de</a></li>
    </ul>
"""

def home(request):
    return HttpResponse(html_base + """
 <h2>Bienvenidos</h2>
 <p>Esto es la portada.</p>
 """)

def about(request):
    return HttpResponse("""
        <h1>Mi Web Personal</h1>
        <h2>Acerca de</h2>
        <p>Me llamo Héctor y me encanta Django!</p>
    """)

