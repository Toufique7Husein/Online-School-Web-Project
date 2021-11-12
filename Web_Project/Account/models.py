from django.db import models
from django.db.models.base import Model
from classroom.models import ClassRoom

# Create your models here.

class Student(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    department = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    dateOfBirth = models.DateField(null=True)
    image = models.ImageField(upload_to = 'img', null = True, blank = True)
    classroom = models.ManyToManyField(ClassRoom, null=True, blank=True)
    isStudent = True
    isFaculty = False
    
    #classroom add to the student
    classes = []
    #to check dublicate
    exist_check = set()
    
    
    class All_Class:
        def __init__(self, classroom, faculty):
            self.classroom = classroom
            self.faculty = faculty
        
            
    def enroll(self, token):
        for temp in self.classroom.all():
            if temp.pk in self.exist_check:
                continue
            make_class = self.All_Class(temp, Faculty.objects.get(classroom = token))
            self.exist_check.add(temp.pk)
            self.classes.append(make_class)
            
    def studentClass(self):
        for temp in self.classroom.all():
            if temp.pk in self.exist_check:
                continue
            make_class = self.All_Class(temp, Faculty.objects.get(classroom = temp.id))
            self.exist_check.add(temp.pk)
            self.classes.append(make_class)
            
    def asList(self):
        return self.classes
    
    def __iter__(self):
        return self.classes.__iter__()
    
    def claarClasses(self):
        self.classes.clear()
        
    def claarSet(self):
        self.exist_check.clear()
    
        
    def joinClass(self, clss):
        self.classroom.add(clss)
    
    
    def setFirstName(self, name):
        self.firstName = name;
        
    def setLastName(self, name):
        self.lastName = name
        
    def setDepartment(self, department):
        self.department = department
        
    def setGender(self, gender):
        self.gender = gender
        
    def setDateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth
        
    def setImage(self, image):
        self.image = image
    
    def setPhoneNumber(self, num):
        self.phoneNumber = num
        
    
        
    
    
    
class Faculty(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    department = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length = 15)
    dateOfBirth = models.DateField(null=True)
    image = models.ImageField(upload_to = 'img', null = True, blank = True)
    classroom = models.ManyToManyField(ClassRoom, null=True, blank=True)
    isStudent = False
    isFaculty = True
    
    classes = []
    checkDublicate = set()
    
    class All_Class:
        def __init__(self, classroom, faculty):
            self.classroom = classroom
            self.faculty = faculty
        
    def creat_class(self, title, course_name, section):
        self.classroom.create(title = title, course_name = course_name, section = section)
        
    def allClass(self):
        for temp in self.classroom.all():
            if temp.pk in self.checkDublicate:
                continue
            make_class = self.All_Class(temp, self)
            self.checkDublicate.add(temp.pk)
            self.classes.append(make_class)
            
    def listOfclass(self):
        return self.classes
    
    def __iter__(self):
        return self.classes.__iter__()
    
    def claarClasses(self):
        self.classes.clear()
        
    def clearCheckDublicate(self):
        self.checkDublicate.clear()
    
    def __iter__(self):
        return self.classes.__iter__() 
    def setFirstName(self, name):
        self.firstName = name;
        
    def setLastName(self, name):
        self.lastName = name
        
    def setDepartment(self, department):
        self.department = department
        
    def setGender(self, gender):
        self.gender = gender
        
    def setDateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth
        
    def setImage(self, image):
        self.image = image
        
    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber
        
        
#this class will about upload reading metarila
class ReadingMaterial(models.Model):
    title = models.CharField(max_length=120)
    assignDate = models.DateTimeField(auto_now_add = True, blank=True)
    dueDate = models.DateField(blank=True)
    paper = models.FileField(upload_to = 'read_material', null = True, blank = True)
    classroom = models.ForeignKey(ClassRoom, null = True, on_delete = models.SET_NULL)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    
