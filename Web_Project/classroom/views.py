from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from Account.models import Student, Faculty, ReadingMaterial
from .models import ClassRoom
from .classDemo import classForFaculty, classForStudent
from material.models import Massage
from django.http import FileResponse, Http404

# Create your views here.

def classroom(request):
    email = request.session['key']
    try:
        faculty = Faculty.objects.get(email = email) 
        faculty.claarClasses()
        faculty.clearCheckDublicate()
        faculty.allClass()
        #print("okkk")
        for st in faculty.__iter__():
            print(st.classroom.title + " " + st.classroom.course_name)
        return render(request, 'classroom.html', {'user' : faculty})
    except:
        student = Student.objects.get(email = email)
        
        student.claarClasses()
        student.claarSet()
        
        student.studentClass()
        for st in student.__iter__():
            print(st.classroom.title)
        return render(request, 'classroom.html', {'user' : student})
  
        
def creatclass(request):
    email = request.session['key']
    if request.method == 'POST':
        title = request.POST['title']
        subject = request.POST['subject']
        section = request.POST['section']
       # try:
        faculty = Faculty.objects.get(email = email)
        faculty.creat_class(title, subject, section)
        last_added_id = ClassRoom.objects.last()
        token = 999 + last_added_id.id
        print(faculty.id)
        msg = Massage.objects.create(cls_code = token, faculty_id = faculty.id)
        msg.save()
        return render(request, 'classroom.html', {'user' : faculty})
        #except:
            #return render(request, 'classroom.html')
    else:
        return render(request, 'creatclass.html')

#students join the class room using their pass
#this fuction will call when the joinclass from submit
def joinclass(request):
    email = request.session['key']
    if request.method == 'POST':
        token = request.POST['code']
        val = int(token)
        val -= 999
        student = Student.objects.get(email = email)
        clss = ClassRoom.objects.get(id = val)
        student.joinClass(clss)
        student.enroll(val)
        return render(request, 'classroom.html', {'user' : student})
    else:
        return render(request, 'joinclass.html')
    
    
#for enter a certain class or classroom
def enterClass(request, id):
    request.session['cls_id'] = id
    email = request.session['key']
    try:
        student = Student.objects.get(email = email)
        cfs = classForStudent()
        cfs.putKeyOfClassroomKey(id)
        clss = ClassRoom.objects.get(id = id)
        return render(request, 'class_for_studen.html', { 'user' : student, 'class' : clss})
    except:
        faculty = Faculty.objects.get(email = email)
        clss = ClassRoom.objects.get(id = id)
        return render(request, 'class_for_faculty.html', {'user' : faculty, 'class' : clss})


#view of enroll students and faculty   
def people(request):
    id = request.session['cls_id']
    email = request.session['key']
    print(id)
    try:
        faculty = Faculty.objects.get(email = email)
        cff = classForFaculty()
        cff.putKeyOfClassroomKey(id)
        return render(request, 'people.html', {'user' : faculty, 'people' : cff})
    except:
        student = Student.objects.get(email = email)
        student.studentClass()
        cfs = classForStudent()
        cfs.putKeyOfClassroomKey(id)
        return render(request, 'people.html', {'user' : student, 'people' : cfs})
    
    
def upload_material(request):
    email = request.session['key']
    if request.method == 'POST' and request.FILES['file']:
        title = request.POST['title']
        due = request.POST['dateOfBirth']
        file = request.FILES['file']
        
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        url = fs.url(filename)
        
        Faculty.objects.get(email = email)
        cls_id = request.session['cls_id']
        faculty = Faculty.objects.get(email = email) 
        
        upload = ReadingMaterial.objects.create(title = title, dueDate = due, paper = url, classroom_id = cls_id, faculty_id = faculty.id)
        upload.save()
        
        return render(request, 'class_for_faculty.html')
    else:   
        email = request.session['key']
        faculty = Faculty.objects.get(email = email)
        return render(request, 'upload_material.html', { 'user' : faculty})
    
