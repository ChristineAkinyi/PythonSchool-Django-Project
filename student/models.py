# from django.db import models
# from course.models import Course
# from schoolclass.models import Schoolclass
# from datetime import date

# # Create your models here.

# class Student(models.Model):
#     # courses = Course.ManyToManyField(Course)
#     courses = models.ManyToManyField('course.Course', related_name='students')
#     student_id = models.AutoField(primary_key=True,default=0)
#     first_name = models.CharField(max_length=20,default='name')
#     last_name = models.CharField(max_length=20,default='country')
#     email = models.EmailField(default='email')
#     code = models.PositiveSmallIntegerField(default=0)
#     date_of_birth = models.DateField(default=date.today)
#     country = models.CharField(max_length=20,default='country')
#     bio = models.TextField(default='bio')
#     guardian_name = models.CharField(max_length=255,default='gn')
#     gender = models.CharField(max_length=30,default='gender')  
#     class_enrolled = models.ForeignKey(Schoolclass, on_delete=models.SET_NULL, null=True, related_name='students')
    

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    
from django.db import models
# from course.models import Course
from schoolclass.models import Schoolclass
from datetime import date

class Student(models.Model):
    # ManyToManyField to Course with a unique related_name
    courses = models.ManyToManyField('course.Course', related_name='students')
    
    # Primary key field, default is unnecessary since AutoField is automatically generated
    student_id = models.AutoField(primary_key=True)
    
    # Ensure defaults are sensible and avoid setting default for fields that shouldn't have one
    first_name = models.CharField(max_length=20, default='name')
    last_name = models.CharField(max_length=20, default='surname')  # Updated default to 'surname'
    email = models.EmailField(default='email@example.com')  # Default email should be more realistic
    code = models.PositiveSmallIntegerField(default=0)
    date_of_birth = models.DateField(default=date.today)
    country = models.CharField(max_length=20, default='country')
    bio = models.TextField(default='bio')
    guardian_name = models.CharField(max_length=255, default='guardian_name')  # Updated default to 'guardian_name'
    gender = models.CharField(max_length=30, default='gender')
    
    # ForeignKey with null=True, appropriate for optional relationships
    class_enrolled = models.ForeignKey(Schoolclass, on_delete=models.SET_NULL, null=True, related_name='students')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

 

   


        
