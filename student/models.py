from django.db import models
# from course.models import Course
from datetime import date
from schoolclass.models import Schoolclass  

class Student(models.Model):
    # Uncomment and use the correct import if necessary
    # courses = models.ManyToManyField(Course, related_name='students')
    
    student_id = models.AutoField(primary_key=True)    
    first_name = models.CharField(max_length=20, default='John')
    last_name = models.CharField(max_length=20, default='Doe')
    email = models.EmailField(default='email@example.com')
    code = models.PositiveSmallIntegerField(default=0)
    date_of_birth = models.DateField(default=date.today)  # Using date.today as callable
    country = models.CharField(max_length=20, default='Country')
    bio = models.TextField(default='No bio provided')
    guardian_name = models.CharField(max_length=255, default='Guardian Name')
    gender = models.CharField(max_length=30, default='Not Specified')
    class_enrolled = models.ForeignKey(Schoolclass, on_delete=models.SET_NULL, null=True, related_name='students')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
