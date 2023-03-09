from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.




class Teacher(models.Model):
    name = models.CharField(null=False, max_length=100)
    email = models.CharField(null=True, max_length=100)
    phone = models.CharField(null=True, max_length=10)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.name






class User(AbstractUser):

    def __str__(self):
        return (self.first_name + " " + self.last_name)

class Course(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(null=False, max_length=100, unique=True)
    description = models.TextField(null=True)
    price = models.CharField(null=False, max_length=100)
    create_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name


class register(models.Model):
    register_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

