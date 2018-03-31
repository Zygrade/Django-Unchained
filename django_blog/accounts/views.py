from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == 'POST':
        UCform = UserCreationForm(request.POST)
        if UCform.is_valid():
            # login
            user = UCform.save()
            login(request,user)
            return redirect('article:list')
    else:
        UCform = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':UCform})

def login_view(request):
    if request.method == 'POST':
        Aform = AuthenticationForm(data=request.POST)
        if Aform.is_valid():
            #login
            user = Aform.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('article:list')
    else:
        Aform = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':Aform})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('article:list')
