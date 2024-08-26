from django.shortcuts import render
# from forms import StudentRegistrationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer, SchoolclassSerializer, StudentSerializer, TeacherSerializer, ClassperiodSerializer, MinimalClassperiodSerializer, MinimalStudentSerializer, MinimalSchoolclassSerializer, MinimalCourseSerializer, MinimalTeacherSerializer
from classperiod.models import ClassPeriod
from course.models import Course
from student.models import Student
from schoolclass.models import Schoolclass
from teacher.models import Teacher

class StudentListView(APIView):
    # def get(Self,request):
    #     students = Student.objects.all()
    #     serializer = MinimalStudentSerializer(students, many=True)
    #     return Response(serializer.data)
    def get(self, request):
        student = Student.objects.all()
        first_name = request.query_params.get("first_name")
        country = request.query_params.get("country")

        if first_name:
            students = students.filter(first_name = first_name)
        country = request.query_params.get("country")
        if country:
            students = students.filter(country = country)

        serializer = MinimalStudentSerializer(student, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
            
class StudentDetailView(APIView):
    def get(self, request,id):
        student = Student.objects.get(id=id)
        serializer = MinimalStudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request,id):
        students = Student.objects.get(id=id)
        serializer = StudentSerializer(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        students = Student.objects.get(id=id)
        students.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    # def enroll(self, student, course_id):
    #     course = Course.objects.get(id=course_id)
    #     student.courses.add(course)
    # def unenroll(self, student, course_id):
    #     course = Course.objects.get(id=course_id)
    #     student.courses.remove(course)
    # def add_to_class(self, student, class_id):
    #     student_class = Student_Class.objects.get(id=class_id)
    #     student_class.students.add(student)

    def post(self, request, id):
        students = Student.objects.get(id=id)
        action = request.data.get("action")
        if action == "enroll":
            course_id = request.data.get("course_id")
            course = Course.objects.get(id=course_id)
            students.courses.add(course)
            # self.enroll(student, course_id)
            return Response(status=status.HTTP_201_CREATED)
        
        elif action == "unenroll":
            course_id = request.data.get("course_id")
            course = Course.objects.get(id=course_id)
            students.courses.remove(course)
            # self.unenroll(student, course_id)
            return Response(status=status.HTTP_200_OK)
        
        elif action == "add_to_class":
            class_id = request.data.get("class_id")
            student_class = Student.objects.get(id=class_id)
            student_class.students.add(students)
            # self.add_to_class(student, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
         return Response(status=status.HTTP_400_BAD_REQUEST)

class TeacherListView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class TeacherDetailView(APIView):
    def get(self, request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_course":
            course_id = request.data.get("course_id")
            course = Course.objects.get(id=course_id)
            teacher.courses.add(course)
            # self.assign_course(teacher, course_id)
            return Response(status=status.HTTP_201_CREATED)
        
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            student_class =Student.objects.get(id=class_id)
            student_class.teacher = teacher
            student_class.save()
            # self.assign_class(teacher, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class CourseDetailView(APIView):
    def get(self, request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self, request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class SchoolclassListView(APIView):
    def get(self, request):
        school_classes = Schoolclass.objects.all()
        serializer = SchoolclassSerializer(school_classes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SchoolclassSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class SchoolclassDetailView(APIView):
    def get(self, request,id):
        school_class = Schoolclass.objects.get(id=id)
        serializer = SchoolclassSerializer(school_class)
        return Response(serializer.data)
    
    def put(self, request,id):
        school_class = Schoolclass.objects.get(id=id)
        serializer = SchoolclassSerializer(school_class, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        school_class = Schoolclass.objects.get(id=id)
        school_class.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class ClassperiodListView(APIView):
    def get(self, request):
        classperiods = ClassPeriod.objects.all()
        serializer = ClassperiodSerializer(classperiods, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer =ClassperiodSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class ClassperiodDetailView(APIView):
    def get(self, request,id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassperiodSerializer(classperiod)
        return Response(serializer.data)
    
    def put(self,request,id):
        classperiod= ClassPeriod.objects.get(id=id)
        serializer = ClassperiodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def post(self, request, id):
        action = request.data.get("action")
        if action == "create_class_period":
            teacher_id = request.data.get("teacher_id")
            course_id = request.data.get("course_id")
            teacher = Teacher.objects.get(id=teacher_id)
            course = Course.objects.get(id, course_id)
            classperiod = ClassPeriod(teacher=teacher, course= course)
            classperiod.save()
            # self.create_class_period(teacher_id, course_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class Timetable(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassperiodSerializer(class_periods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # def create_class_period(self, teacher_id, course_id):
    #     teacher = Teacher.objects.get(id=teacher_id)
    #     course = Course.objects.get(id=course_id)
    #     class_period = Classperiod(teacher=teacher, course=course)
    #     class_period.save()
    #     return Response(status=status.HTTP_201_CREATED)

# from django.shortcuts import render
# from .serializers import ClassperiodSerializer, CourseSerializer, MinimalClassperiodSerializer, MinimalCourseSerializer, MinimalSchoolclassSerializer, MinimalStudentSerializer, MinimalTeacherSerializer, SchoolclassSerializer, StudentSerializer, TeacherSerializer
# from classperiod.models import ClassPeriod
# from course.models import Course
# from student.models import Student
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from schoolclass.models import Schoolclass
# from teacher.models import Teacher
# from rest_framework import status

# # Create your views here.
# class StudentListView(APIView):
#     def get(self, request):
#         student = Student.objects.all()
#         first_name = request.query_params.get("first_name")
#         if first_name: 
#             Students = Students.filter(first_name = first_name)
#         country = request.query_params.get("country")
#         if country:
#             Students = Students.filter(country = country)
#         serializer = StudentSerializer(student, many=True)
#         serializer = MinimalStudentSerializer(student, many = True)
#         return Response(serializer.data)
       
#     def post(self, request):
#         serializer = StudentSerializer(data =request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
# class StudentDetailView(APIView):
#     def get(self, request,id):
#         student = Student.objects.get(id=id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
    
#     def put(self, request,id):
#         student = Student.objects.get(id=id)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete (self, request, id):
#         student = Student.objects.get(id=id)
#         student.delete()
#         return Response(status=status.HTTP_202_ACCEPTED)
    
#     def enroll(self, student, course_id):
#         course = Course.objects.get(id=course_id)
#         student.courses.add(course)

#     def unenroll(self, student, course_id):
#         course = Course.objects.get(id=course_id)
#         student.courses.remove(course)
    
#     def add_to_class(self, student, class_id):
#         schoolclasses = Schoolclass.objects.get(id=class_id)
#         schoolclasses.students.add(student)

#     def post(self, request, id):
#         student = Student.objects.get(id=id)
#         action = request.data.get("action")
#         if action == "enroll":
#             course_id = request.data.get("course_id")
#             self.enroll(student, course_id)
#             return Response(status=status.HTTP_201_CREATED)
#         elif action == "unenroll":
#             course_id = request.data.get("course_id")
#             self.unenroll(student, course_id)
#             return Response(status=status.HTTP_200_OK)
#         elif action == "add_to_class":
#             class_id = request.data.get("class_id")
#             self.add_to_class(student, class_id)
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#          return Response(status=status.HTTP_400_BAD_REQUEST)  
    
# class TeacherListView(APIView):
#     def get(self, request):
#         teachers = Teacher.objects.all()
#         serializer = TeacherSerializer(teacher, many=True)
#         serializer = MinimalTeacherSerializer(teachers, many = True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = TeacherSerializer(data =request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
# class TeacherDetailView(APIView):
#     def get(self, request,id):
#         teachers = Teacher.objects.get(id=id)
#         serializer = TeacherSerializer(teachers)
#         return Response(serializer.data)
    
#     def put(self, request,id):
#         teachers = Teacher.objects.get(id=id)
#         serializer = TeacherSerializer(teachers, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete (self, request, id):
#         teachers = Teacher.objects.get(id=id)
#         teachers.delete()
#         return Response(status=status.HTTP_202_ACCEPTED)
    
#     def assign_course(self, teacher, course_id):
#         courses = Course.objects.get(id=course_id)
#         teacher.courses.add(courses)

#     def assign_class(self, teacher, class_id):
#         schoolclass = Schoolclass.objects.get(id=class_id)
#         schoolclass.teacher = teacher
#         schoolclass.save()
    
#     def post(self, request, id):
#         teachers = Teacher.objects.get(id=id)
#         action = request.data.get("action")
#         if action == "assign_course":
#             course_id = request.data.get("course_id")
#             self.assign_course(teachers, course_id)
#             return Response(status=status.HTTP_201_CREATED)
#         elif action == "assign_class":
#             class_id = request.data.get("class_id")
#             self.assign_class(teachers, class_id)
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
    
# class CourseListView(APIView):
#     def get(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         serializer = MinimalCourseSerializer(courses, many = True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializers = CourseSerializer(data =request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.errors,status= status.HTTP_400_BAD_REQUEST)
        
# class CourseDetailView(APIView):
#     def get(self, request,id):
#         courses = Course.objects.get(id=id)
#         serializer = CourseSerializer(courses)
#         return Response(serializer.data)
    
#     def put(self, request,id):
#         courses = Course.objects.get(id=id)
#         serializers = CourseSerializer(courses, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete (self, request, id):
#         courses = Course.objects.get(id=id)
#         courses.delete()
#         return Response(status=status.HTTP_202_ACCEPTED)

# class SchoolclassListView(APIView):
#     def get(self, request):
#         schoolclasses = Schoolclass.objects.all()
#         serializers = SchoolclassSerializer(schoolclasses, many=True)
#         serializers = MinimalSchoolclassSerializer(schoolclasses, many = True)
#         return Response(serializers.data)
    
#     def post(self, request):
#         serializers = SchoolclassSerializer(data =request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.errors,status= status.HTTP_400_BAD_REQUEST)
        
# class SchoolclassDetailView(APIView):
#     def get(self, request,id):
#         schoolclasses = Schoolclass.objects.get(id=id)
#         serializers = SchoolclassSerializer(schoolclasses)
#         return Response(serializers.data)
    
#     def put(self, request,id):
#         schoolclasses = Schoolclass.objects.get(id=id)
#         serializers = SchoolclassSerializer(schoolclasses, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete (self, request, id):
#         schoolclasses = Schoolclass.objects.get(id=id)
#         schoolclasses.delete()
#         return Response(status=status.HTTP_202_ACCEPTED)

# class ClassperiodListView(APIView):
#     def get(self, request):
#         classperiods = ClassPeriod.objects.all()
#         serializers = ClassperiodSerializer(classperiods, many=True)
#         serializers = MinimalClassperiodSerializer(classperiods, many = True)
#         return Response(serializers.data)
    
#     def post(self, request):
#         serializers =ClassperiodSerializer(data =request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.errors,status= status.HTTP_400_BAD_REQUEST)
        
# class ClassperiodDetailView(APIView):
#     def get(self, request,id):
#         classperiods = ClassPeriod.objects.get(id=id)
#         serializers = ClassperiodSerializer(classperiods)
#         return Response(serializers.data)
    
#     def put(self,request,id):
#         classperiods= ClassPeriod.objects.get(id=id)
#         serializers = ClassperiodSerializer(classperiods, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete (self, request, id):
#         classperiods = ClassPeriod.objects.get(id=id)
#         classperiods.delete()
#         return Response(status=status.HTTP_202_ACCEPTED)
    
#     def post(self, request, id):
#         action = request.data.get("action")
#         if action == "create_class_period":
#             teacher_id = request.data.get("teacher_id")
#             course_id = request.data.get("course_id")
#             self.create_class_period(teacher_id, course_id)
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#     def create_class_period(self, teacher_id, course_id):
#         teacher = Teacher.objects.get(id=teacher_id)
#         course = Course.objects.get(id=course_id)
#         class_period = ClassPeriod(teacher=teacher, course=course)
#         class_period.save()
#         return Response(status=status.HTTP_201_CREATED)
    
     
# class Timetable(APIView):
#     def get(self, request):
#         classperiods = ClassPeriod.objects.all()
#         serializer = ClassperiodSerializer(classperiods, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

