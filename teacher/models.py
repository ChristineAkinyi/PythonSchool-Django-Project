from django.db import models
from student.models import Student


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_first_name = models.CharField(max_length=40, default='John')
    teacher_last_name = models.CharField(max_length=40, default='Doe')
    teacher_email = models.EmailField(max_length=254, default='email@example.com')
    phone_number = models.CharField(max_length=20, blank=True, default='N/A')
    department = models.CharField(max_length=20, default='General')
    photo = models.ImageField(upload_to='photos/', default='photos/default.jpg')
    address = models.CharField(max_length=100, blank=True, default='Unknown')
    date_of_birth = models.DateField(null=True, blank=True)
    salary = models.PositiveSmallIntegerField(default=0)
    student = models.ForeignKey(
        'student.Student', 
        blank=True, 
        null=True, 
        on_delete=models.SET_NULL, 
        related_name='teachers'
    )

    def __str__(self):
        return f"{self.teacher_first_name} {self.teacher_last_name}"
