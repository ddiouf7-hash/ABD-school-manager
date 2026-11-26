from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentForm
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


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f"{student} a été inscrit(e).")
            return redirect(f"/students/{student.id}/")
    else:
        form = StudentForm()
    context = {"form": form, "title": "Inscrire un étudiant"}
    return render(request, "students/student_form.html", context)

def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'student': student})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})