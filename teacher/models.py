from django.db import models

# Create your models here.

class Teacher(models.Model):
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE, default=1)
    teacher_id = models.PositiveSmallIntegerField()
    teacher_first_name = models.CharField(max_length=20)
    teacher_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    photo = models.ImageField()
    experience = models.CharField(max_length=20)
    teacher_last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    salary = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.teacher_id} {self.teacher_last_name}"