from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Bienvenue a ABD")

def student_list(request):
    return HttpResponse("Liste des etudiants ")

def student_detail(request, id):
    return HttpResponse(f"Detail de l'etudiant {id}")