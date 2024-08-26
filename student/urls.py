from django.urls import path
from .import views
# dot=current directory

urlpatterns = [
    path("register/", views.register_student, name="register"),
]