from django.shortcuts import render

# Create your views here.
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse

class Tarefa(object):
    def __init__(self, titulo, data):
        self.titulo=titulo
        self.data=data
    def __str__(self):
        return self.titulo


def home(request):
    return HttpResponse("Olá")
def sobre(request):
    return HttpResponse("Mari Caramello")
def tarefa(request, numero):
    return HttpResponse("Tarefa: "+str(numero))
def tarefa(request, ano, mes, dia):
    return HttpResponse("Tarefa: "+str(ano)+"/"+str(mes)+"/"+str(dia))
def nome(request):
    return HttpResponse("Maria do Carmo")
