from django.shortcuts import render

from rest_framework import status

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
from schoolclass.models import Schoolclass
from .serializers import SchoolclassSerializer

class SchoolclassListView(APIView):
    def get (self,request):
        schoolclass =Schoolclass.objects.all()
        serializer =SchoolclassSerializer(schoolclass, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SchoolClassSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentListView(APIView):
    """
    class for student list view
    """
    def get(self,request):
        """ function for get"""
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self,request):
        """function for post"""
        serializer = StudentSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class TeacherListView(APIView):
    """ class for teacher list view"""
    def get(self, request):
        """get function"""
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        """post function"""
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class CourseListView(APIView):
    """course list view class"""
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        """post function"""
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

class ClassPeriodListView(APIView):
    """classperiod list view class"""
    def get(self, request):
        classperiod = Classperiod.objects.all()
        serializer=  ClassperiodSerializer(classperiod, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClassperiodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
        

class StudentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    
    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response (status=status.HTTP_202_ACCEPTED)

class CourseDetailView(APIView):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = Course.objects.get(id=id)
        serializer= CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response (status=status.HTTP_202_ACCEPTED)

class ClassperiodDetailView(APIView):
    def get(self, request, id):
        classperiod = Classperiod.objects.get(id=id)
        serializer = ClassperiodSerializer(classperiod)
        return Response(serializer.data)
    

    def put (self,request, id):
        classperiod = Classperiod.objects.get(id=id)
        serializer = ClassperiodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        classperiod = Classperiod.objects.get(id=id)
        classperiod.delete()
        return Response (status=status.HTTP_202_ACCEPTED)

class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
      
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
     
class SchoolclassDetailView(APIView):
    def get(self, request, id):
        schoolclass = Schoolclass.objects.get(id=id)
        serializer = SchoolclassSerializer(schoolclass, many=True)
        return Response(serializer.data)
    
    def put(self, request, id):
        schoolclass = Schoolclass.objects.get(id=id)
        serializer = SchoolclassSerializer(schoolclass, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        schoolclass = Schoolclass.objects.get(id=id)
        schoolclass.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

