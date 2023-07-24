from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User

from .forms import LoginForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method =='POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            # form.instance.username = f'{random.randrange(10000000)}'
            # form.instance.username = form.instance.phone
            form.save()
            # phone =form.cleaned_data.get('phone')      
            messages.success(request,f'Account created for successfully')
            return redirect('/')
    else:
        form =RegisterForm()
    return render(request, 'userapp/register.html',{'form':form})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_super_admin:
                login(request, user)
                return redirect('homee')
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('dashboard-home')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('dashboard-home')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('dashboard-home')
            elif user is not None and user.is_user:
                login(request, user)
                return redirect('home')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'userapp/login.html', {'form': form, 'msg': msg})

@login_required
def profile(request):
    return render(request, 'userapp/profile.html')

@login_required
def profileupdate(request):

    if request.method == 'POST':
        u_form = UpdateRegisterForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile-update')
    else:
        u_form =  UpdateRegisterForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)

    context = {

        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'userapp/profileupdate.html', context)





