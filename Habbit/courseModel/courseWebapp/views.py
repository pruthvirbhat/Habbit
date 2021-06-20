from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Courses
from . serializers import CoursesSerializer
from . import serializers

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/course-list/',
        'Detail View': '/course-detail/<str:pk>/',
        'Create': '/course-create/',
        'Update': '/course-update/<str:pk>/',
        'Delete': '/course-delete/<str:pk>/',
        'Add To Wishlist':'Courses/course-add-to-wishlist/',

    }
    return Response(api_urls)

@api_view(['GET'])
def courseList(request):
    course1 = Courses.objects.all()
    serializer = CoursesSerializer(course1,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def courseDetail(request,pk):
    course1 = Courses.objects.get(id=pk)
    serializer = CoursesSerializer(course1,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def courseCreate(request):
    serializer = CoursesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def courseUpdate(request,pk):
    course1 = Courses.objects.get(id=pk)
    serializer = CoursesSerializer(course1, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def courseDelete(request,pk):
    course1 = Courses.objects.get(id=pk)
    course1.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

