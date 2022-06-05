from django.shortcuts import render, redirect
from apps.users.forms import LoginForm, UpdateProfileForm
from apps.settings.models import Setting
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from apps.users.models import User
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        profile_image = request.FILES.get('profile_image')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            try:
                user = User.objects.create(username = username, first_name = first_name, last_name = last_name, profile_image = profile_image, email = email)
                user.set_password(password1)
                user.save()
                return redirect('index')
            except:
                messages.error(request, "Error")
            
        else:
            messages.error(request, 'Пароли отличаются')
    return render(request, 'account/signup.html')

    

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def user_profile(request, id):
    user = User.objects.get(id = id)
    home = Setting.objects.latest('id')
    context = {
        'user' : user,
        'home' : home,
    }
    return render(request, 'account/my-profile.html', context)

def update_profile(request, id):
    user = User.objects.get(id = id)
    form = UpdateProfileForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_profile', user.id)
    context = {
        'form' : form,
    }
    return render(request, 'account/update.html', context)

def delete_profile(request, id):
    user = User.objects.get(id = id)
    if request.method == "POST":
        user.delete()
        return redirect('index')
    return render(request, 'account/delete.html')