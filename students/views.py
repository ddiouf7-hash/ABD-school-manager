from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Student

def home(request):
    context = {
        'school_name': "Ecole d'Excellence de Dakar",
        'description': "Bienvenue sur notre plateforme"
    }
    return render(request, 'students/home.html', context)

def about(request):
    return render(request, 'students/about.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/student_detail.html', {'student': student})

def teacher_list(request):
    return HttpResponse("<h1>Liste des profs - a venir</h1>")

def course_list(request):
    return HttpResponse("<h1>Liste des cours - a venir</h1>")