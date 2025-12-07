from django.urls import path
from . import views

urlpatterns = [
path('sample_page',views.sample_message,name='sample'),
path('demo_page',views.demo_message,name='demo'),
path('third_page',views.third_message,name='third'),
path('', views.home, name='home'),
path('add/', views.add_student, name='add_student'),
path('edit/<int:id>/', views.edit_student, name='edit_student'),
path('delete/<int:id>/', views.delete_student, name='delete_student'),

path('courses/', views.course_list, name='course_list'),
path('courses/add/', views.course_add, name='course_add'),
path('courses/edit/<int:course_id>/', views.course_edit, name='course_edit'),
path('courses/delete/<int:course_id>/', views.course_delete, name='course_delete'),

path('attendance/', views.attendance_list, name='attendance_list'),
path('attendance/add/', views.attendance_add, name='attendance_add'),
path('attendance/edit/<int:attendance_id>/', views.attendance_edit, name='attendance_edit'),
path('attendance/delete/<int:attendance_id>/', views.attendance_delete, name='attendance_delete'),

path('teacher/', views.teacher_list, name='teacher_list'),
path('teacher/add/', views.teacher_add, name='teacher_add'),
path('teacher/edit/<int:teacher_id>/', views.teacher_edit, name='teacher_edit'),
path('teacher/delete/<int:teacher_id>/', views.teacher_delete, name='teacher_delete'),

path('marks/', views.marks_list, name='marks_list'),
path('marks/add/', views.marks_add, name='marks_add'),
path('marks/edit/<int:marks_id>/', views.marks_edit, name='marks_edit'),
path('marks/delete/<int:marks_id>/', views.marks_delete, name='marks_delete'),


path('subjects/', views.subject_list, name='subject_list'),
path('subjects/add/', views.subject_add, name='subject_add'),
path('subjects/edit/<int:subject_id>/', views.subject_edit, name='subject_edit'),
path('subjects/delete/<int:subject_id>/', views.subject_delete, name='subject_delete'),
]