from django.urls import path
from .views import (
    StudentListView, StudentDetailView,
    ClassperiodListView, ClassperiodDetailView,
    CourseListView, CourseDetailView,
    TeacherListView, TeacherDetailView,
    SchoolclassListView, SchoolclassDetailView,
    Timetable
)

urlpatterns = [
    path("Student/", StudentListView.as_view(), name="student_list_view"),
    path('api/Student/', StudentListView.as_view(), name='student_list_view'),

    
    path("Classperiod/", ClassperiodListView.as_view(), name="classperiod_list_view"),
    path("Classperiod/<int:id>/", ClassperiodDetailView.as_view(), name="classperiod_detail_view"),
    
    path("course/", CourseListView.as_view(), name="course_list_view"),
    path("course/<int:id>/", CourseDetailView.as_view(), name="course_detail_view"),
    
    path("Teacher/", TeacherListView.as_view(), name="teacher_list_view"),
    path("Teacher/<int:id>/", TeacherDetailView.as_view(), name="teacher_detail_view"),
    
    path("schoolclass/", SchoolclassListView.as_view(), name="schoolclass_list_view"),
    path("schoolclass/<int:id>/", SchoolclassDetailView.as_view(), name="schoolclass_detail_view"),
    
    path('timetable/', Timetable.as_view(), name='timetable'),
]
