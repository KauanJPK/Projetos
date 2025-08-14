from django.shortcuts import render
from django.http import HttpResponse
from . import templates

def entrada(request):
    return render(request, 'entrada.html')
