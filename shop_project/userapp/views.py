from django.shortcuts import render,redirect

from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method =='POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')      
            messages.success(request,f'Account created for {username}! You are now able to login')
            return redirect('home')
    else:
        form =RegisterForm()
    return render(request, 'userapp/registration.html',{'form':form})

@login_required
def profile_func(request):
    return render(request, 'userapp/profile.html')


def profile_update_func(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Account Updated')
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context ={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,  'userapp/profile-update.html',context)
    