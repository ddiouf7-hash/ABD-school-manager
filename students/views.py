from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Bienvenue a ABD")

def student_list(request):
    return HttpResponse("Liste des etudiants ")

def student_detail(request, id):
    return HttpResponse(f"Detail de l'etudiant {id}")

def about(request):
    return HttpResponse("A propos de l'ecole ABD - Projet Django 2026")

def teacher_list(request):
    return HttpResponse("Liste des enseignants")

def course_list(request):
    return HttpResponse("Liste des cours")

