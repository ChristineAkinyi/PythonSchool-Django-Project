from django.db import models

# Create your models here.

# class Student(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     date_of_birth = models.DateField()
#     id = models.AutoField(primary_key=True)
#     code = models.PositiveSmallIntegerField(unique=True)
#     gender = models.CharField(max_length=10)
#     country = models.CharField(max_length=100)
#     bio = models.TextField(blank=True, null=True)
#     enrollment_date = models.DateField()
#     guardian_phone_number = models.CharField(max_length=15)
#     guardian_name = models.CharField(max_length=100)
#     classes = models.ManyToManyField(Class, related_name='students', blank=True)
#     courses = models.ManyToManyField(Course, related_name='students', blank=True)
#     # class_enrolled = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='students')
#     picture = models.ImageField()
    
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()
    guardian = models.CharField(max_length=255, default='Unknown')
    gender = models.CharField(max_length=255, default='Unknown')    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

 

   


        
