from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateCustomUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from qa.models import questions, answers

# Create your views here.
def UserSignup(request):
    signup_form = CreateCustomUserForm()
    if request.method == "POST":
        signup_form = CreateCustomUserForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return HttpResponse("User Created")
        else:
            print("not valid")
    else:
        print("method is not post")
    return render(request,'user/signup.html',{"form":signup_form})


def UserSignin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return HttpResponse("Login Success")
        else:
            return HttpResponse("User Does not Exist")
    return render(request,'user/signin.html',{})


login_required(login_url="/user/signin")
def UserSignout(request):
    logout(request)
    return redirect('/user/signin')


login_required(login_url="/user/signin")
def UserProfile(request):
    context = {}
    profile = request.user
    context['profile'] = profile
    try:
        context['questions'] = questions.objects.filter(asked_by=profile)
    except:
        context['questions'] = None
    return render(request,"user/profile.html",context)
