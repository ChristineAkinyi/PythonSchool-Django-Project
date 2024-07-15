from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from course.models import Course
from .serializers import CourseSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from classperiod.models import Classperiod
from .serializers import ClassperiodSerializer

class StudentListView(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(Course, many=True)
        return Response(serializer.data)

class ClassPeriodListView(APIView):
    def get(self, request):
         classperiod = Classperiod.objects.all()
         serializer = ClassperiodSerializer(Classperiod, many=True)
         return Response(serializer.data)




# Create your views here.
