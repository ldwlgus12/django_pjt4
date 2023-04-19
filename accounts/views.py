from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('balances:index')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('balances:index')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('balances:index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form})
    

@login_required
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('balances:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('balances:index')
    else:
        form = CustomUserChangeForm(instance=request.user)    
    return render(request, 'accounts/update.html', {'form' : form})