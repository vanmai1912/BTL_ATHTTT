from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, permissions
from .models import Course, User, Teacher, register, Category
from .serializers import CourseSerializer, UserSerializer, registerSerializer, TeacherSerializer, CategorySerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView,
                  generics.RetrieveAPIView
                  ):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class registerViewSet(viewsets.ModelViewSet):
    queryset = register.objects.all()
    serializer_class = registerSerializer





def index(request):
    return HttpResponse("e-courses app")



# Create your views here.
