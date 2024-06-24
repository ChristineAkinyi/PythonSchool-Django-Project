from django.db import models

# Create your models here.

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
    

 

   


        
