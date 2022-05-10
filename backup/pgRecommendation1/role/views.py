from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Admin, Member , appointmentP , Chat , Prescription
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.core.files.storage import FileSystemStorage
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
import os
from datetime import date
import jwt
import requests
import json
from time import time

def home(request):
    if request.method == 'POST':
        if request.POST.get("sa"):
            return redirect(registerA)
        if request.POST.get("sm"):
            return redirect(registerM)
    return render(request, 'role/landing.html')

def dashboardM(request):
    username = request.user.username
    user_id = request.user.id
    mt=Member.objects.all() # Collect all records from table 
                            
    return render(request, 'role/dashboardM.html', {'username':username , 'user_id':user_id , 'mt':mt } )


def addPropertyM(request):
    username = request.user.username
    user_id = request.user.id
    mt=Member.objects.all() # Collect all records from table 
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("addPropertyM"):
            mt=Member.objects.all() # Collect all records from table
                            
    return render(request, 'role/addPropertyM.html', {'username':username , 'user_id':user_id , 'mt':mt } )

def searchPropertyM(request):
    username = request.user.username
    user_id = request.user.id
    mt=Member.objects.all() # Collect all records from table 
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("searchPropertyM"):
            mt=Member.objects.all() # Collect all records from table
                            
    return render(request, 'role/searchPropertyM.html', {'username':username , 'user_id':user_id , 'mt':mt } )


def dashboardA(request):
    username = request.user.username
    admin_id = request.user.id
    at=Admin.objects.all() # Collect all records from table 
    mt=Member.objects.all() # Collect all records from table 
    return render(request, 'role/dashboardA.html', {'username':username , 'admin_id':admin_id ,  'at':at , 'mt':mt } )

def editProfileM(request , user_id):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("editProfileM"):
            print("edit profile user_id:" + str(user_id))            
            mt=Member.objects.all() # Collect all records from table
            for mts in mt :
                if mts.user_id == user_id :
                    uname = request.POST['username']
                    mno = request.POST['mobilenumber']
                    email = request.POST['email']
                    password = request.POST['pw1']
                    wa = request.POST['wa']
                    spc = request.POST['spc']
                    fee = request.POST['fee']
                    
                    mts.name = uname
                    mts.email = email
                    mts.mobileNumber = mno
                    mts.password = password
                    mts.workingAddress = wa
                    mts.specialization = spc
                    mts.fee = fee
                    mts.save()
                    break
            
            return redirect('dashboardM')
    username = request.user.username
    user_id = request.user.id
    mt=Member.objects.all() # Collect all records from table 
    return render(request, 'role/editProfileM.html', {'username':username , 'user_id':user_id , 'mt':mt } )

def editProfileA(request , admin_id):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("editProfileA"):
            print("edit profile admin_id:" + str(admin_id))            
            at=Admin.objects.all() # Collect all records from table
            for ats in at :
                if ats.user_id == admin_id :
                    uname = request.POST['username']
                    mno = request.POST['mobilenumber']
                    email = request.POST['email']
                    password = request.POST['pw1']
                    ats.name = uname
                    ats.email = email
                    ats.mobileNumber = mno
                    ats.password = password
                    ats.save()
                    break
            
            return redirect('dashboardA')
    username = request.user.username
    admin_id = request.user.id
    at=Admin.objects.all() # Collect all records from table 
    return render(request, 'role/editProfileA.html', {'username':username , 'admin_id':admin_id , 'at':at } )

def registerA(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("signupA"):
            print("hello")
            print(request.POST)
            uname = request.POST['username']
            mno = request.POST['mobilenumber']
            name = request.POST['name']
            gender = request.POST['gender']
            email = request.POST['email']
            password = request.POST['pw1']
            us = User.objects.create_user(uname, email, password)
            std = Admin.objects.create(
                user=us, name=name, gender=gender ,  email=email, mobileNumber=mno)
            messages.success(request, f'Your account has been created! You are now able to log in')
            return render(request,'role/loginA.html')
        if request.POST.get("loginA"):
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboardA')
            else:
                messages.success(request, f'Wrong Credentials')
    return render(request, 'role/loginA.html')


def registerM(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("signupM"):
            print("hello")
            print(request.POST)
            uname = request.POST['username']
            mno = request.POST['mobilenumber']
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['pw1']
            workingaddres=request.POST['wa']
            spc=request.POST['spc']
            fees=request.POST['fee']
           
            us = User.objects.create_user(uname, email, password)
            std = Member.objects.create(
                user=us, name=name, email=email, mobileNumber=mno,workingAddress=workingaddres , fee=fees, specialization=spc)
            messages.success(request, f'Your account has been created! You are now able to log in')
            return render(request,'role/loginM.html')
        if request.POST.get("loginM"):
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboardM')
            else:
                messages.success(request, f'Wrong Credentials')
    return render(request, 'role/loginM.html')
    
def logout(request):
    return render(request, 'role/logout.html')

def doctors(request):
    dt=Doctor.objects.all() # Collect all records from table 
    return render(request,'role/doctors.html',{'dt':dt})

def patients(request):
    pt=Patient.objects.all() # Collect all records from table 
    return render(request,'role/patients.html',{'pt':pt})

def suicide_test(request , patient_id):
    print("suicide_test:" + str(patient_id))
    if request.POST.get("suicide_test"):
        answer1 = request.POST['answer1']
        answer2 = request.POST['answer2']
        answer3 = request.POST['answer3']
        response = do_something(patient_id , answer1 , answer2 , answer3)
        print("response:", response)
        messages.success(request, response)
    
        return render(request,'role/suicide_test.html' , {'patient_id':patient_id , 'response':response})
    
    return render(request,'role/suicide_test.html' , {'patient_id':patient_id , 'response':''})

    
def get_appointment(request , doctor_id):
    print("get_appointment:" + str(doctor_id))
    print(request.POST)
    if request.POST.get("book_appointment"):
        print("book_appointment:" + str(doctor_id))
        appointment_date = request.POST['appointment_date']
        appointment_time = request.POST['appointment_time']
        amount = request.POST['amount']
        doc_id = request.POST['doctor_id']
        how = request.POST['how']
        print(appointment_date)
        print(appointment_time)   
        print(amount)   
        print(doc_id)   
        print(how) 
        apt = appointmentP.objects.create(date=appointment_date, time=appointment_time, how=how, doctor_id=doc_id, patient_id=request.user.id , amount=amount)            
        dt=Doctor.objects.all() # Collect all records from table 
        today = date.today()        
        return render(request,'role/book_appointment.html' , {'doctor_id':doctor_id , 'dt':dt , 'today':today})
    else:    
        dt=Doctor.objects.all() # Collect all records from table 
        today = date.today()
        return render(request,'role/book_appointment.html' , {'doctor_id':doctor_id , 'dt':dt , 'today':today})
    
def charts(request):
    return render(request,'role/charts.html')   
    
def breadcrumb_pagination(request):
    return render(request,'role/breadcrumb_pagination.html')   

def prescription(request , patient_id):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        file_name = os.path.basename(file_url)
        pt=Patient.objects.all() # Collect all records from table
        doctor_id=request.user.id
        
        prescription = Prescription.objects.create(from_id=doctor_id, to_id=patient_id , image=file_name)
    return render(request, 'role/prescription.html' , {'patient_id':patient_id })

    
def uploadM(request , doctor_id):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        file_name = os.path.basename(file_url)
        dt=User.objects.all() # Collect all records from table
        count =0        
        updated_row=0
        for dts in dt :
            count = count + 1
            if dts.user_id == doctor_id :
                updated_row = count
                dts.image = file_name
                dts.save()

        return redirect('dashboardU')
    return render(request, 'role/uploadU.html')
    
def uploadA(request , patient_id):
    print("upload patient_id:" + str(patient_id))
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        print(upload.name)
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        print(file_url)
        
        file_name = os.path.basename(file_url)
        pt=Admin.objects.all() # Collect all records from table
        count =0        
        updated_row=0
        for pts in pt :
            count = count + 1
            if pts.user_id == patient_id :
                updated_row = count
                pts.image = file_name
                pts.save()

        return redirect('dashboardA')
    return render(request, 'role/uploadA.html')
    
def chatP(request , from_id , to_id , pd):  #pd=1 patient , pd=2 doctor
    if request.method == 'POST':
        message = request.POST['message']
        print(message)
        chat = Chat.objects.create(from_id=from_id, to_id=to_id , message=message)
    
    
    dt=Doctor.objects.all() # Collect all records from table   
    pt=Patient.objects.all() # Collect all records from table   
    chat=Chat.objects.all() # Collect all records from table 
    return render(request,'role/chatP.html' , {'from_id':from_id , 'to_id':to_id  , 'dt':dt , 'pt':pt , 'chat':chat , 'pd':pd})   

def prescriptionP(request):  
    dt=Doctor.objects.all() # Collect all records from table   
    pt=Patient.objects.all() # Collect all records from table   
    prescription=Prescription.objects.all() # Collect all records from table 
    patient_id=request.user.id
    print("patient_id:", patient_id)
    return render(request,'role/prescriptionP.html' , {'patient_id':patient_id , 'dt':dt , 'pt':pt , 'prescription':prescription})   


def chatD(request , from_id , to_id , pd):  #pd=1 patient , pd=2 doctor
    if request.method == 'POST':
        message = request.POST['message']
        print(message)
        chat = Chat.objects.create(from_id=from_id, to_id=to_id , message=message)
    
    
    dt=Doctor.objects.all() # Collect all records from table   
    pt=Patient.objects.all() # Collect all records from table   
    chat=Chat.objects.all() # Collect all records from table 
    return render(request,'role/chatD.html' , {'from_id':from_id , 'to_id':to_id  , 'dt':dt , 'pt':pt , 'chat':chat , 'pd':pd})   

def videoP(request , from_id , to_id , pd):  #pd=1 patient , pd=2 doctor
    if request.method == 'POST':
        message = request.POST['message']
        print(message)
    
    
    payload = {'exp': time() + 5000,
           'iss': 'KT7_jK0MRXui0D3KpcL8EA'    
          }     
    token = jwt.encode(payload, 'rLOMNSVkcABthVss1qnelEUAuXBJsFyRHR3J' , algorithm='HS256')

    #conn = http.client.HTTPSConnection("api.zoom.us")
    headers = {
            'authorization': "Bearer " + token,
            'content-type': "application/json"
              }
    
    # create json data for post requests
    meetingdetails = {"topic": "Online Medicare zoom meeting",
                  "type": 2,
                  "start_time": "2021-12-01T16: 30: 00",
                  "duration": "45",
                  "timezone": "Europe/Madrid",
                  "agenda": "test",
  
                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }
  
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings', 
      headers=headers, data=json.dumps(meetingdetails))
  
    print("\n creating zoom meeting ... \n")
    # print(r.text)
    # converting the output into json and extracting the details
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]
  
    print(
        f'\n here is your zoom meeting link {join_URL} and your \
        password: "{meetingPassword}"\n')
  
    subject = 'Zoom Meeting Request Online Medicare'
    message = f'\n here is your zoom meeting link {join_URL} and your \
        password: "{meetingPassword}"\n'
    from_email = 'celab2010@gmail.com'
    to_email = ''
    
    pt=Patient.objects.all() # Collect all records from table   
    for pts in pt :
        if pts.user_id == from_id :
            to_email = [pts.email]

    if subject and message and from_email and to_email:
        try:
            send_mail(subject, message, from_email, to_email)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    
    to_email = ''
    dt=Doctor.objects.all() # Collect all records from table   
    for dts in dt :
        if dts.user_id == to_id :
            to_email = [dts.email , ]
    
    if subject and message and from_email and to_email:
        try:
            send_mail(subject, message, from_email, to_email)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    
                
    return render(request,'role/videoP.html' , {'from_id':from_id , 'to_id':to_id  , 'dt':dt , 'pt':pt , 'join_URL':join_URL , 'meetingPassword':meetingPassword })   
