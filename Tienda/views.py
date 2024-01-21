from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Producto

def home(request):
    productos = Producto.objects.all()
    return render(request, 'Tienda/home.html', {'productos': productos})

def hombre(request):
    productos = Producto.objects.all()
    return render(request, 'ropa/hombre.html', {'productos': productos})

def mujer(request):
    productos = Producto.objects.all()
    return render(request, 'ropa/mujer.html', {'productos': productos})

def logout_view(request):
    logout(request)
    return render(request, 'Tienda/home.html')

def registro(request):
    data = {'form': CustomUserCreationForm()}

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/register.html', data)

def contacto(request):
    return render(request, 'Tienda/contacto.html')

def compra(request):
    if request.method == 'POST':
        messages.success(request, 'Compra realizada con éxito.')
        return redirect('home')
    # Resto del código si el método de solicitud no es POST
    return render(request, 'compra/compra.html')