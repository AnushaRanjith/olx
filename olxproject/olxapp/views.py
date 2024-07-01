from django.db.models.query import QuerySet
from django.shortcuts import render,redirect

from django.views import View
from django.http import HttpResponse
from olxapp.forms import UserRegisterForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from olxapp.models import OlxModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class UserRegister(CreateView):
    model=OlxModel
    form_class=UserRegisterForm
    template_name='register.html'
    success_url=reverse_lazy('home.html')

    def post(self,request):
        data=UserRegisterForm(request.POST)
        if data.is_valid():
            formdata=data.cleaned_data
            User.objects.create_user(**formdata)
            return HttpResponse("saved")
        else:
            return HttpResponse("invalid credentials")
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')

class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,'login.html',{'form':form})  
    def post(self,request):
        customer=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=customer,password=psw)
        if user:
            login(request,user)
            messages.success(request,'login successfull')
            return redirect('userlogin_view')
        else:
            messages.error(request,'invalid credentials')
            return redirect('Home_view')
class LogoutView(View) :
    def get(self,request):
        return redirect('Home_view')

