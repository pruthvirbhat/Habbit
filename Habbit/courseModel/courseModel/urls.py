"""courseModel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from courseWebapp import views


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Courses/', views.apiOverview),
    path('Courses/course-list/', views.courseList),
    path('Courses/course-detail/<str:pk>/', views.courseDetail),
    path('Courses/course-create/', views.courseCreate),
    path('Courses/course-update/<str:pk>/', views.courseUpdate),
    path('Courses/course-delete/<str:pk>/', views.courseDelete),
    # path('Courses/course-add-to-wishlist/', views.addCourseToWishList),
    # path('Courses/course-view-wishlist/',views.wishList.as_view()),
    # path('Courses/course-add-to-wishlist/',views.wishListDetail.as_view()),

]