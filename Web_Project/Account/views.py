from Account.models import Faculty, Student
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from onlineschool.Notification import Notifications
#Create your views here.

def login(request):
    ntf = Notifications();
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
    
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            try:
                request.session['key'] = username
                st = Student.objects.get(email = username)
                return render(request, 'home.html', {'user': st, 'ntf':ntf})
            except:
                request.session['key'] = username
                ft = Faculty.objects.get(email = username)
                return render(request, 'home.html',{'user': ft})        
        else:
            return render(request, 'login.html')
        
    else:
        return render(request, 'login.html')
    


    
def logout(request):
    auth.logout(request)
    return redirect('/')



def signup(request):
    if request.method == 'POST' and request.FILES['image']:
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        who = request.POST['who']
        gender = request.POST['gender']
        phoneNumber = request.POST['phoneNumber']
        email = request.POST['email']
        dateOfBirth = request.POST['dateOfBirth']
        firstPass = request.POST['firstPass']
        conformPass = request.POST['lastPass']
        image = request.FILES['image']
        
        print(type(image))
        
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        url = fs.url(filename)
        
       # print(type(url))
        
        if firstPass == conformPass:
            if User.objects.filter(email = email).exists():
               messages.info(request, 'this eamil already exist')
               print("exists")
               return render(request, 'signup.html')
            else:               
                if who == "Faculty": 
                    faculty = Faculty.objects.create(firstName = firstName, lastName = lastName, gender = gender, department = "please update",email = email, phoneNumber = phoneNumber, image = url, dateOfBirth = dateOfBirth)
                    faculty.save()
                    #print("faculty created")
                else:
                    student = Student.objects.create(firstName = firstName, lastName = lastName, gender = gender, department = "please update",email = email, phoneNumber = phoneNumber, image = url, dateOfBirth = dateOfBirth)
                    student.save()
                    #print("student created")
                 #valid pass and email adress can join 
                user = User.objects.create_user(username = email, password = firstPass, last_name = lastName, first_name = firstName, email = email)  
                user.save()
                messages.info(request, 'You signed up, succesfully')  
                return redirect('/')
        else:
            messages.info(request, 'both password have to same')
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')
    

