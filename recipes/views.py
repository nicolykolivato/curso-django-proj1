from django.http import HttpResponse
from django.shortcuts import render


# HTTP Request
def home(request):
    return HttpResponse('Home 1')
    # http response

def contato(request):
    return HttpResponse('Contato')

def sobre(request):
    return HttpResponse('Sobre')
