from django.urls import path
from .views import StudentListView

urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),

]