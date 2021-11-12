from django.contrib import admin
from .models import Student, Faculty, ReadingMaterial
from classroom.models import ClassRoom
from material.models import PhotoOfReader, Question,Answer, Massage

# Register your models here.
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(ClassRoom)
admin.site.register(ReadingMaterial)
admin.site.register(PhotoOfReader)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Massage)