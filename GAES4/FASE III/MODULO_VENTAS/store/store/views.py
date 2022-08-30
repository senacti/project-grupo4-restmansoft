from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages


def index(request):
    return render(request, 'index.html', {
        'mensaje': 'Lista de productos'
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.name))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrecto')

    return render(request, 'login.html', {
    })


def logout_view(request):
    logout (request)
    messages.success(request, 'Sesión Finalizada')
    return redirect ('index') 


def dashboardAdmin(request):
    return render(request, 'dashboardAdmin.html', {
    })


def dashboardCliente(request):
    return render(request, 'dashboardCliente.html', {
    })


def productos(request):
    return render(request, 'productos.html', {
    })


def registrarnuevocliente(request):
    return render(request, 'registrarnuevocliente.html', {
    })
