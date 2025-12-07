from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.student_add, name='student_add'),
    path('edit/<int:id>/', views.student_edit, name='student_edit'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),



    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_add, name='course_add'),
    path('courses/edit/<int:id>/', views.course_edit, name='course_edit'),
    path('courses/delete/<int:id>/', views.course_delete, name='course_delete'),


    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.attendance_add, name='attendance_add'),
    path('attendance/edit/<int:id>/', views.attendance_edit, name='attendance_edit'),
    path('attendance/delete/<int:id>/', views.attendance_delete, name='attendance_delete'),

    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/add/', views.subject_add, name='subject_add'),
    path('subjects/edit/<int:id>/', views.subject_edit, name='subject_edit'),
    path('subjects/delete/<int:id>/', views.subject_delete, name='subject_delete'),

    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.teacher_add, name='teacher_add'),
    path('teachers/edit/<int:id>/', views.teacher_edit, name='teacher_edit'),
    path('teachers/delete/<int:id>/', views.teacher_delete, name='teacher_delete'),
    path('marks/', views.marks_list, name='marks_list'),
    path('marks/add/', views.marks_add, name='marks_add'),
    path('marks/edit/<int:id>/', views.marks_edit, name='marks_edit'),
    path('marks/delete/<int:id>/', views.marks_delete, name='marks_delete'),
]


