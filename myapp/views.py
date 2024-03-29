from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import feature

# Create your views here.
def index(request):
    #name='NAVEEN' #sending dynamic data to our template file
    #context={'name':'naveen','age':18,'nationality':'india'}# dictionary to send dynamically to template file
    # return render(request,'index.html',context)#{'name':name}
    # feature1=feature()
    # # feature1.id=0
    # feature1.name='naveen'
    # # feature1.is_true=True
    # feature1.details='i am finding my way'

    # feature2=feature()
    # # feature2.id=1
    # feature2.name='naveen'
    # # feature2.is_true=True
    # feature2.details='i am finding my way'

    # feature3=feature()
    # # feature3.id=2
    # feature3.name='naveen'
    # # feature3.is_true=False
    # feature3.details='i am finding my way'

    # feature4=feature()
    # # feature4.id=3
    # feature4.name='naveen'
    # # feature4.is_true=True
    # feature4.details='i am finding my way'
    
    # features=[feature1,feature2,feature3,feature4]
    features=feature.objects.all()
    return render(request,'indexe.html',{'features':features})
   
    # return render(request,'index.html',{feature:feature1})

def counter(request):
    # text=request.POST['text']
    # amount_of_words=len(text.split())
    posts=[1,2,3,'naveen','praveen']
    return render(request, 'counter.html', {'posts':posts})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if  User.objects.filter(email=email).exists():
                messages.info(request,'Email Already exists')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')   

            else:
                user=User.objects.create_user(username=username,email=email,password=password)  
                user.save();
                return redirect('login')
        
        else:
            messages.info(request,'Password are mismatched')
            return redirect('register')

    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username , password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request,'Invalid Credentials')

    else:        
        return render(request, 'login.html')  

def logout(request):
    auth.logout(request)
    return redirect('/')

def create(request):
    return render(request,'register.html')   

def post(request,pk):
    return render(request,'post.html',{'pk':pk})    