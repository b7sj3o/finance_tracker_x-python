from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ..forms import RegisterUserForm, LoginUserForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(
                    request, ('Ви успішно увійшли до акаунту!'))
                return redirect('home')
            else:
                messages.error(
                    request, ('Неправильний логін чи пароль. Спробуйте знову'))
                return redirect('login_user')
        else:
            print("Form is not valid")
    else:
        form = LoginUserForm()
        
    context = {
        "form": form
    }

    return render(request, 'login.html', context)

@login_required
def logout_user(request):
    try:
        logout(request)
        messages.success(request, 'Ви вийшли з акаунту')
    except Exception as ex:
        messages.error(request, f'Трапилася помилка, {ex}')
        
    return redirect('home')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = RegisterUserForm()
    
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            login(request, user)
            
            return redirect('home')
        
    
    context = {
        "form": form
    }
    return render(request, "register.html", context)