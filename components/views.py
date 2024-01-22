from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def header(request):
    return render(request, "tareas.html",{'title':"Header para ver si funciona"})