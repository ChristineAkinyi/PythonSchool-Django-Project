from django.db import models
# from datetime import date

# Create your models here.

class Teacher(models.Model):
    
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    teacher_id = models.AutoField(primary_key=True)
    teacher_first_name = models.CharField(max_length=40, default='first_name')
    teacher_email = models.EmailField(default='email_address')
    phone_number = models.CharField(max_length=20, default='phone_number')
    department = models.CharField(max_length=20, default='department')
    photo = models.ImageField(upload_to='photos/', default='default.jpg')
    address = models.CharField(max_length=20, default='address')
    teacher_last_name = models.CharField(max_length=40, default='last_name')
    # date_of_birth = models.DateField(default=date.today())
    salary = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return f"{self.teacher_last_name}"