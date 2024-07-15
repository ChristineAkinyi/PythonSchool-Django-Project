# from rest_framework import se/rializers

from rest_framework import serializers
from student.models import Student
# from class.models import Class
from classperiod.models import Classperiod
from teacher.models import Teacher
from course.models import Course





class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class ClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classperiod
        fields = "__all__"

# class ClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Class
#         fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"




