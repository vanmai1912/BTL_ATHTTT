from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("categories", views.CategoryViewSet)
router.register("courses", views.CourseViewSet)
router.register("users", views.UserViewSet)
router.register("teachers", views.TeacherViewSet)
router.register("register", views.registerViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
