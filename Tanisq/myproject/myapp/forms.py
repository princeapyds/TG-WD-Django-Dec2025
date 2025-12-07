from django import forms
from .models import Attendance
from .models import Course, Subject, StudentCourse
from django.contrib.auth.models import User

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'description']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'course', 'teacher']

class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = ['student', 'course']

class AssignStudentForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = ['student', 'course']