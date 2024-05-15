from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, RegistrationForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('all_products')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all_products')
    else:
        form = RegistrationForm()
    return render(request, 'account/registration.html', {'form': form})
