from django.db.models.fields import DateTimeField
from Account.models import Student, Faculty
from classroom.models import ClassRoom
from django.db import models


# Create your models here.
class PhotoOfReader(models.Model):
    image = models.ImageField(upload_to = 'img', null = True, blank = True)
    classroom = models.ForeignKey(ClassRoom, null = True, on_delete = models.SET_NULL)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)


class Question(models.Model):
    question = models.CharField(max_length=200)
    classroom = models.ForeignKey(ClassRoom, null = True, on_delete = models.SET_NULL)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    
class Answer(models.Model):
    question = models.OneToOneField(Question, primary_key=True, on_delete=models.CASCADE)
    anser = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    
class Massage(models.Model):
    curretnTIme = models.DateTimeField(auto_now = True)
    cls_code = models.IntegerField(null=True)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    