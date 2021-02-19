from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,ClaimForm,MotorClaimForm,LifeClaimForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

# # User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)     
            messages.success(request, f'Account created for {username}')
            return redirect('select_category')
    else:
        form = UserRegisterForm()
    context={
        'form':form
    }
    return render(request, 'auth/register.html',context)


# @login_required
# def application_submitted(request):
#     applications = Application.objects.all()
#     return render(request, 'submitted.html', {
#         'applications': applications
#     })



@login_required
def home(request):
    user=request.user
    if (user.is_superuser or user.is_staff):
        return HttpResponseRedirect('/admin/')
    else:
        return render(request,'home.html')


@login_required
def select_category(request):
    if request.method == 'POST':
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim=form.save(commit=False)
            claim.applicant=request.user
            claim=form.save()
            category = form.cleaned_data.get('category')
            if category == 'Motor Claim':
                return redirect('motor_claim')
            else:
                return redirect('life_claim')
        
    else:
        form = ClaimForm()
    return render(request, 'category.html', {
        'form': form
    })


@login_required
def motor_claim(request):
    if request.method == 'POST':
        form = MotorClaimForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Files uploaded successfully!!')
            return redirect('submitted')
    else:
        form = MotorClaimForm()
    return render(request, 'motor_claim.html', {
        'form': form
    })


@login_required
def life_claim(request):
    if request.method == 'POST':
        form = LifeClaimForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Files uploaded successfully!!')
            return redirect('submitted')
    else:
        form = LifeClaimForm()
    return render(request, 'life_claim.html', {
        'form': form
    })




# @login_required
# def log_out(request):
#     
#     return redirect('application_list')


