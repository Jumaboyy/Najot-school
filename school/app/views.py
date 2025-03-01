from rest_framework import viewsets
from .models import Class, Teacher, Student
from .serializers import ClassSerializer, TeacherSerializer, StudentSerializer
from rest_framework import permissions

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
