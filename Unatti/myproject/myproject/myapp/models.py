from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_description = models.TextField()

    def __str__(self):
        return self.course_name


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.EmailField(unique=True)
    qualification = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()

class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.EmailField()
    qualification = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Marks(models.Model):
    EXAM_CHOICES = [
        ('Midterm', 'Midterm'),
        ('Final', 'Final'),
        ('Quiz', 'Quiz'),
    ]
    student_id = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    exam_type = models.CharField(max_length=20, choices=EXAM_CHOICES)