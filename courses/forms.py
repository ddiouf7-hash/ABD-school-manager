from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'teacher']
        labels = {
            'title': 'Titre du cours',
            'description': 'Description',
            'teacher': 'Enseignant',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Mathématiques'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
        }