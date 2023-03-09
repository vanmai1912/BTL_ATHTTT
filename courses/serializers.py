from rest_framework.serializers import ModelSerializer
from .models import Course, User, Teacher, Category, register


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CourseSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Course
        fields = ["id", "name", "description", "price", "category"]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "password"]
        extra_kwargs = {
            'password': {'write_only': 'True'}

        }


    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "name", "phone", "email", "description"]





class registerSerializer(ModelSerializer):
    course = CourseSerializer()
    user = UserSerializer()
    class Meta:
        model = register
        fields = ["id", "register_date", "course", "user"]
