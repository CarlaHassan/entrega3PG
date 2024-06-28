from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def productos(request):
    context={}
    return render(request, 'productos.html', context) 

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def formulario(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        archivo = request.FILES['archivo']
        sexo = request.POST['sexo']
        birthdate = request.POST['birthdate']
        pais = request.POST['pais']
        terminos_condiciones = request.POST.get('terminos_condiciones', False)

        return HttpResponse('Formulario enviado correctamente!')
    return render(request, 'formulario.html')

def galeria(request):
    return render(request, 'myapp/galeria.html')
    
