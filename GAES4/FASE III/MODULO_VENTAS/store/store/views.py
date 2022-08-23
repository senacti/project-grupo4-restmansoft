from django.shortcuts import render

def index(request):
    return render(request,'index.html',{
        'mensaje': 'Lista de productos'
        })


def Login(request):
    return render(request,'Login.html',{

        })


