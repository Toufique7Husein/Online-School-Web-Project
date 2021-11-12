from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from Account.models import Student, Faculty, ReadingMaterial
from classroom.models import ClassRoom
from material.models import PhotoOfReader, Question
# Create your views here.

#list of all material
def materials(request):
    email = request.session['key']
    class_id = request.session['cls_id']
    try:
        student = Student.objects.get(email = email)
        list = []
        list = ReadingMaterial.objects.filter(classroom_id = class_id)
        context = {'user' : student, 'lom' : list}  
        return render(request, 'materials.html', context)   
    except:
        faculty = Faculty.objects.get(email = email)
        list = []
        list = ReadingMaterial.objects.filter(classroom_id = class_id)
        print(len(list))
        context = {'user' : faculty, 'lom' : list}
        return render(request, 'materials.html', context)

#this function help to open pdf and capture photo from webcome automatically
def readPdf(request, id):
    email = request.session['key']
    cls_key = request.session['cls_id']
    if request.method == 'POST':
      questions = request.POST['question']
      read = ReadingMaterial.objects.get(id = id)
       # print(read.title)
      return render(request, 'pdf.html', {'user': read})
    
    #cls_id = request.session['cls_id']
        
    try:
        print(email)
        read = ReadingMaterial.objects.get(id = id)
        print(read.title)
        return render(request, 'pdf.html', {'user': read})
            
    except:
        print(email)
        read = ReadingMaterial.objects.get(id = id)
        print(read.title)
        return render(request, 'pdf.html', {'user': read})
