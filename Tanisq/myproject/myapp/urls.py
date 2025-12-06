from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/edit/<int:id>/', views.edit_course, name='edit_course'),
    path('courses/delete/<int:id>/', views.delete_course, name='delete_course'),

    path('subject/', views.subject_list, name='subject_list'),
    path('subject/add/', views.add_subject, name='add_subject'),
    path('subject/edit/<int:id>/', views.edit_subject, name='edit_subject'),
    path('subject/delete/<int:id>/', views.delete_subject, name='delete_subject'),

    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('teachers/edit/<int:id>/', views.edit_teacher, name='edit_teacher'),
    path('teachers/delete/<int:id>/', views.delete_teacher, name='delete_teacher'),

    path('attendance/mark/', views.mark_attendance, name='mark_attendance'),
    path('attendance/list/', views.attendance_list, name='attendance_list'),
    path('attendance/summary/', views.monthly_summary, name='monthly_summary'),
    path('attendance/export/', views.export_attendance, name='export_attendance'),

    path('marks/', views.marks_list, name='marks_list'),
    path('marks/add/', views.add_marks, name='add_marks'),

    path('login/', views.login_page, name='login'),
]
