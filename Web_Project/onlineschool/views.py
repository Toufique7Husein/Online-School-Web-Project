from .Notification import Notifications
from django.contrib.auth import models
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import auth
from Account.models import Student, Faculty

# Create your views here.
# controler of home.html
def home(request):
    ntf = Notifications()
    
    print(len(ntf.notifications))
    
    for a in ntf.notifications:
        print(a.faculty.firstName)
    
   
    email = request.session['key']
    try:
        st = Student.objects.get(email = email)
        return render(request, 'home.html', {'user' : st, 'ntf' : ntf})
    except:
        ft = Faculty.objects.get(email = email)
        return render(request, 'home.html', {'user' : ft, 'ntf': ntf})
        
        
#control Myprofile.html
def profile(request):
    email = request.session['key']
    if request.method == 'POST':
        return render(request, 'MyProfile.html')
    else:
        try:
            st = Student.objects.get(email = email)
            return render(request, 'MyProfile.html', {'user' : st})
        except:
            ft = Faculty.objects.get(email = email)
            return render(request, 'MyProfile.html', {'user' : ft})
        
        
        
#control edit profile      
def edit_profile(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        datOfBirth = request.POST['dateOfBirth']
        phoneNumber = request.POST['phoneNumber']
        gender = request.POST['gender']
        department = request.POST['department']
        email= request.session['key']
        
        try:
            st = Student.objects.get(email = email)
            st.setFirstName(firstName)
            st.setLastName(lastName)
            st.setDateOfBirth(datOfBirth)
            st.setPhoneNumber(phoneNumber)
            st.setDepartment(department)
            st.setGender(gender)
            st.save()
            return render(request, 'Myprofile.html', {'user' : st})
        except:
            ft = Faculty.objects.get(email = email)
            ft.setFirstName(firstName)
            ft.setLastName(lastName)
            ft.setDateOfBirth(datOfBirth)
            ft.setPhoneNumber(phoneNumber)
            ft.setDepartment(department)
            ft.setGender(gender)
            ft.save()
            return render(request, 'Myprofile.html', {'user' : ft})
    else:
        email= request.session['key']
        try:
            st = Student.objects.get(email = email)
            return render(request, 'EditProfile.html', {'user' : st})
        except:
            ft = Faculty.objects.get(email = email)
            return render(request, 'EditProfile.html', {'user' : ft})
        
