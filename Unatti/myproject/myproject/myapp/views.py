from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Attendance, Teacher, Subject, Marks



def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        age = request.POST['age']
        Student.objects.create(name=name, email=email, course=course, age=age)
        return redirect('student_list')
    return render(request, 'student_add.html')

def student_edit(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.age = request.POST['age']
        student.save()
        return redirect('student_list')
    return render(request, 'student_edit.html', {'student': student})

def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')



def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_add(request):
    if request.method == 'POST':
        name = request.POST['course_name']
        description = request.POST['course_description']
        Course.objects.create(course_name=name, course_description=description)
        return redirect('course_list')
    return render(request, 'course_add.html')

def course_edit(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        course.course_name = request.POST['course_name']
        course.course_description = request.POST['course_description']
        course.save()
        return redirect('course_list')
    return render(request, 'course_edit.html', {'course': course})

def course_delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('course_list')


def attendance_list(request):
    records = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'records': records})

def attendance_add(request):
    students = Student.objects.all()
    if request.method == 'POST':
        student = Student.objects.get(id=request.POST['student'])
        date = request.POST['date']
        status = request.POST['status']
        Attendance.objects.create(student=student, date=date, status=status)
        return redirect('attendance_list')
    return render(request, 'attendance_add.html', {'students': students})

def attendance_edit(request, id):
    record = Attendance.objects.get(id=id)
    students = Student.objects.all()
    if request.method == 'POST':
        record.student = Student.objects.get(id=request.POST['student'])
        record.date = request.POST['date']
        record.status = request.POST['status']
        record.save()
        return redirect('attendance_list')
    return render(request, 'attendance_edit.html', {'record': record, 'students': students})

def attendance_delete(request, id):
    record = Attendance.objects.get(id=id)
    record.delete()
    return redirect('attendance_list')


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects_list.html', {'subjects': subjects})

def subject_add(request):
    courses = Course.objects.all()  # for FK dropdown
    if request.method == 'POST':
        name = request.POST['name']
        course_id = request.POST['course_id']
        course = get_object_or_404(Course, id=course_id)
        Subject.objects.create(name=name, course=course)
        return redirect('subject_list')
    return render(request, 'subjects_add.html', {'courses': courses})

def subject_edit(request, id):
    subject = get_object_or_404(Subject, id=id)
    courses = Course.objects.all()
    if request.method == 'POST':
        subject.name = request.POST['name']
        course_id = request.POST['course_id']
        subject.course = get_object_or_404(Course, id=course_id)
        subject.save()
        return redirect('subject_list')
    return render(request, 'subjects_edit.html', {'subject': subject, 'courses': courses})

def subject_delete(request, id):
    subject = get_object_or_404(Subject, id=id)
    subject.delete()
    return redirect('subjects_list')


# ---------------- Teacher Views ----------------

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def teacher_add(request):
    courses = Course.objects.all()  # for FK dropdown
    if request.method == 'POST':
        name = request.POST['name']
        emailid = request.POST['emailid']
        qualification = request.POST['qualification']
        course_id = request.POST['course_id']
        course = get_object_or_404(Course, id=course_id)
        Teacher.objects.create(
            name=name,
            emailid=emailid,
            qualification=qualification,
            course=course
        )
        return redirect('teacher_list')
    return render(request, 'teacher_add.html', {'courses': courses})

def teacher_edit(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    courses = Course.objects.all()
    if request.method == 'POST':
        teacher.name = request.POST['name']
        teacher.emailid = request.POST['emailid']
        teacher.qualification = request.POST['qualification']
        course_id = request.POST['course_id']
        teacher.course = get_object_or_404(Course, id=course_id)
        teacher.save()
        return redirect('teacher_list')
    return render(request, 'teacher_edit.html', {'teacher': teacher, 'courses': courses})

def teacher_delete(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return redirect('teacher_list')


def marks_list(request):
    marks = Marks.objects.all()
    return render(request, 'marks_list.html', {'marks': marks})

def marks_add(request):
    subjects = Subject.objects.all()
    if request.method == 'POST':
        student_id = request.POST['student_id']
        subject = Subject.objects.get(id=request.POST['subject'])
        marks_value = request.POST['marks']
        exam_type = request.POST['exam_type']
        Marks.objects.create(student_id=student_id, subject=subject, marks=marks_value, exam_type=exam_type)
        return redirect('marks_list')
    return render(request, 'marks_add.html', {'subjects': subjects})

def marks_edit(request, id):
    mark = Marks.objects.get(id=id)
    subjects = Subject.objects.all()
    if request.method == 'POST':
        mark.student_id = request.POST['student_id']
        mark.subject = Subject.objects.get(id=request.POST['subject'])
        mark.marks = request.POST['marks']
        mark.exam_type = request.POST['exam_type']
        mark.save()
        return redirect('marks_list')
    return render(request, 'marks_edit.html', {'mark': mark, 'subjects': subjects})

def marks_delete(request, id):
    Marks.objects.get(id=id).delete()
    return redirect('marks_list')