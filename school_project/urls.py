from django.contrib import admin
from django.urls import path
from students.views import student_list, student_detail, student_create, student_update, student_delete
from courses.views import course_list, course_detail, course_create, course_update, course_delete
from pages.views import home, about
from teachers.views import teacher_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('students/', student_list, name='student_list'),
    path('students/new/', student_create, name='student_create'),
    path('students/<int:id>/', student_detail, name='student_detail'),
    path('students/<int:id>/edit/', student_update, name='student_update'),
    path('students/<int:id>/delete/', student_delete, name='student_delete'),
    path('courses/', course_list, name='course_list'),
    path('courses/new/', course_create, name='course_create'),
    path('courses/<int:pk>/', course_detail, name='course_detail'),
    path('courses/<int:pk>/edit/', course_update, name='course_update'),
    path('courses/<int:pk>/delete/', course_delete, name='course_delete'),
]