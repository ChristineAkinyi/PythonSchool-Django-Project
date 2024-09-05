# from django.db import models

# # Create your models here.

# class Teacher(models.Model):
#     student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE, default=1)
#     teacher_id = models.PositiveSmallIntegerField()
#     teacher_first_name = models.CharField(max_length=20)
#     teacher_email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     department = models.CharField(max_length=20)
#     photo = models.ImageField()
#     experience = models.CharField(max_length=20)
#     teacher_last_name = models.CharField(max_length=20)
#     date_of_birth = models.DateField()
#     salary = models.PositiveSmallIntegerField()
#     def __str__(self):
#         return f"{self.teacher_id} {self.teacher_last_name}"

from django.db import models
<<<<<<< HEAD
# Create your models here.
class Teacher(models.Model):
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE, default=1)
    teacher_id = models.AutoField(primary_key=True,default=0)
    teacher_first_name = models.CharField(max_length=40)
    teacher_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    photo = models.ImageField()
    # address = models.CharField(max_length=20)
    teacher_last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    salary = models.PositiveSmallIntegerField()
=======
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

>>>>>>> 2160289272b7422c44a3adec0944456ed2529cb5
    def __str__(self):
        return f"{self.teacher_first_name} {self.teacher_last_name}"
