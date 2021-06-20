from django.db import models
from django.db.models.base import Model

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.ForeignKey(Category,on_delete=models.PROTECT)
    course_name = models.CharField(max_length=40)
    author_name = models.CharField(max_length=40)
    course_date = models.DateField()
    course_price = models.FloatField()
    users_enrolled = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name