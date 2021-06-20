from django.db.models import fields
from rest_framework import serializers
from . models import Category, Courses

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
