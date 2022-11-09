from django.shortcuts import render, HttpResponse
#HttResponse nos permite constar a una petición devolviendo un código
# Create your views here.
html_base = """
    <h1>Mi Web Personal</h1>
    <ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de</a></li>
    <li><a href="/contact/">Contacto</a></li>
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
        <p>Me llamo Carlota y me encantas TÚ!!!!</p>
    """)


def contact(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Aquí os dejo mi email y mis redes sociales:</p>
        <ul>
        <li><a href="mailto:cmartmat@myuax.com">Email</a></li>
        <li><a href="https://github.com/carlotamartin">Github</a></li>
        <li><a href="https://youtube.com">Youtube</a></li>
        </ul>

        """)


