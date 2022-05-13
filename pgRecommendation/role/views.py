from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Admin, Member , Property
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
from random import randint, randrange
import smtplib, ssl
import gmaps

def home(request):
    if request.method == 'POST':
        if request.POST.get("sa"):
            return redirect(registerA)
        if request.POST.get("sm"):
            return redirect(registerM)
    return render(request, 'role/landing.html')

def aboutus(request):
    return render(request, 'role/about.html')

def contactus(request):
    return render(request, 'role/contact.html')

def dashboardM(request):
    username = request.user.username
    user_id = request.user.id
    mt=Member.objects.all() # Collect all records from table 
    prop=Property.objects.all() # Collect all records from table
    
    total_prop=0
    my_prop =0
    for props in prop :
        total_prop = total_prop + 1
        if props.user_name == username:
            my_prop = my_prop + 1 
    return render(request, 'role/dashboardM.html', {'username':username , 'user_id':user_id , 'mt':mt , 'total_prop':total_prop , 'my_prop':my_prop } )


def addPropertyM(request):
    username = request.user.username
    user_id = request.user.id
    mt=Member.objects.all() # Collect all records from table 
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("addPropertyM"):
            user_name = username
            house_name = request.POST['house_name']
            address = request.POST['address']
            rent = request.POST['rent']
            
            facility = ""
            if request.POST.get('facility1'):
                facility1 = request.POST['facility1']
                facility += facility1 + ","
            if request.POST.get('facility2'):
                facility2 = request.POST['facility2']
                facility += facility2 + ","               
            if request.POST.get('facility3'):
                facility3 = request.POST['facility3'] 
                facility += facility3 + ","               
            if request.POST.get('facility4'):
                facility4 = request.POST['facility4'] 
                facility += facility4 + ","               
            
            pgType = ""
            if request.POST.get('pgType1'):
                pgType1 = request.POST['pgType1']
                pgType += pgType1 + ","
            if request.POST.get('pgType2'):
                pgType2 = request.POST['pgType2']
                pgType += pgType2 + ","               
            if request.POST.get('pgType3'):
                pgType3 = request.POST['pgType3'] 
                pgType += pgType3 + ","               
            
            no_of_rooms = request.POST['no_of_rooms']
            near_by_facilities = request.POST['near_by_facilities']
            
            file_name = ""
            if request.FILES['upload']:
                upload = request.FILES['upload']
                fss = FileSystemStorage()
                file = fss.save(upload.name, upload)
                file_url = fss.url(file)
                file_name = os.path.basename(file_url)
                print("file_name:" ,file_url ," ",  file_name)
            
            #configure api
            #gmaps.configure(api_key='AIzaSyCLxOsct_BXA-EQaCZT_grynI7bDFI_7V8')
            #new_york_coordinates = (40.75, -74.00)
            #gmaps.figure(center=new_york_coordinates, zoom_level=12)
            
            
            prop = Property.objects.create(
                user_name=user_name , house_name=house_name , address=address , rent=rent , facility=facility , pg_type=pgType , no_of_rooms=no_of_rooms , near_by_facilities=near_by_facilities , image=file_name)
                        
    return render(request, 'role/addPropertyM.html', {'username':username , 'user_id':user_id , 'mt':mt } )

def addPropertyA(request):
    username = request.user.username
    user_id = request.user.id
    mt=Member.objects.all() # Collect all records from table 
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("addPropertyA"):
            user_name = username
            house_name = request.POST['house_name']
            address = request.POST['address']
            rent = request.POST['rent']
            
            facility = ""
            if request.POST.get('facility1'):
                facility1 = request.POST['facility1']
                facility += facility1 + ","
            if request.POST.get('facility2'):
                facility2 = request.POST['facility2']
                facility += facility2 + ","               
            if request.POST.get('facility3'):
                facility3 = request.POST['facility3'] 
                facility += facility3 + ","               
            if request.POST.get('facility4'):
                facility4 = request.POST['facility4'] 
                facility += facility4 + ","               
            
            pgType = ""
            if request.POST.get('pgType1'):
                pgType1 = request.POST['pgType1']
                pgType += pgType1 + ","
            if request.POST.get('pgType2'):
                pgType2 = request.POST['pgType2']
                pgType += pgType2 + ","               
            if request.POST.get('pgType3'):
                pgType3 = request.POST['pgType3'] 
                pgType += pgType3 + ","               
            
            no_of_rooms = request.POST['no_of_rooms']
            near_by_facilities = request.POST['near_by_facilities']
            
            file_name = ""
            if request.FILES['upload']:
                upload = request.FILES['upload']
                fss = FileSystemStorage()
                file = fss.save(upload.name, upload)
                file_url = fss.url(file)
                file_name = os.path.basename(file_url)
                print("file_name:" ,file_url ," ",  file_name)
            
            prop = Property.objects.create(
                user_name=user_name , house_name=house_name , address=address , rent=rent , facility=facility , pg_type=pgType , no_of_rooms=no_of_rooms , near_by_facilities=near_by_facilities , image=file_name)
                        
    return render(request, 'role/addPropertyA.html', {'username':username , 'user_id':user_id , 'mt':mt } )


def searchPropertyM(request):
    username = request.user.username
    user_id = request.user.id
    mt=Member.objects.all() # Collect all records from table
    prop=Property.objects.all() # Collect all records from table
                
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("searchPropertyM"):
            prop=Property.objects.all() # Collect all records from table
              
    return render(request, 'role/searchPropertyM.html', {'username':username , 'user_id':user_id , 'prop':prop } )

def searchPropertyA(request):
    username = request.user.username
    user_id = request.user.id
    mt=Member.objects.all() # Collect all records from table
    prop=Property.objects.all() # Collect all records from table
                
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("searchPropertyM"):
            prop=Property.objects.all() # Collect all records from table
              
    return render(request, 'role/searchPropertyA.html', {'username':username , 'user_id':user_id , 'prop':prop } )

def showProperty(request , prop_id):
    prop=Property.objects.all() # Collect all records from table
                          
    return render(request, 'role/showProperty.html', {'prop_id':prop_id , 'prop':prop } )

def dashboardA(request):
    username = request.user.username
    admin_id = request.user.id
    at=Admin.objects.all() # Collect all records from table 
    mt=Member.objects.all() # Collect all records from table 
    prop=Property.objects.all() # Collect all records from table
    total_prop=0
    for props in prop :
        total_prop = total_prop + 1
    
    return render(request, 'role/dashboardA.html', {'username':username , 'admin_id':admin_id ,  'at':at , 'mt':mt , 'total_prop':total_prop} )

def editProfileM(request , user_id):
    username = request.user.username
    user_id = request.user.id
    mt=Member.objects.all() # Collect all records from table 
    return render(request, 'role/editProfileM.html', {'username':username , 'user_id':user_id , 'mt':mt } )

def editProfileA(request , admin_id):
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


def otpM(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("otpM"):
            email = request.POST['email']
            otp = request.POST['otp']
            mt=Member.objects.all()   
    
            for mts in mt :
                if mts.email == email and mts.otp == otp :
                    mts.is_enabled = '1'
                    mts.save()
                    return redirect('dashboardM')

    return render(request, 'role/otpM.html')

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
            address=request.POST['wa']
            
            us = User.objects.create_user(uname, email, password)
            num = randrange(111111, 999999)  # randrange is exclusive at the stop

            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "celab2010@gmail.com"  # Enter your address
            receiver_email = email # Enter receiver address
            password = "Anoj123*"
            message = """\
            Subject: Hi there

            Your OTP for Registering to PG Recommendation System is """ + str(num)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
               
   
            std = Member.objects.create(
                user=us, name=name, email=email, mobileNumber=mno,address=address , otp = num , is_enabled='0')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return render(request,'role/loginM.html')
        if request.POST.get("loginM"):
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password , is_enabled='1')
            if user is not None:
                auth_login(request, user)
                return redirect('dashboardM')
            else:
                messages.success(request, f'Wrong Credentials')
    return render(request, 'role/loginM.html')
    
def logout(request):
    return render(request, 'role/logout.html')


    
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
