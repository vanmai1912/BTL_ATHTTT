from django.contrib import admin
from .models import Category, Teacher, User, Course, register

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone", "description"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "last_name", "first_name", "username"]



class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "description", "category", "teacher", "active"]

class registerAdmin(admin.ModelAdmin):
    list_display = ["id", "register_date", "user", "course"]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(register, registerAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Course, CourseAdmin)
