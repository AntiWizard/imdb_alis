from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import SignUpForm, LoginForm


def signup(request):
    if request.method == "GET":
        signup_form = SignUpForm()
        return render(request, 'users/registrations/signup.html',
                      context={'form': signup_form})
    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if not form.is_valid():
            messages.warning(
                request,
                "This user was created before!!"
            )
            return redirect('signup')

    User.objects.create_user(request.POST.get('username'),
                             request.POST.get('email'),
                             request.POST.get('password'))
    messages.success(
        request,
        "You're register successfully!"
    )
    return redirect('login')


def user_login(request):
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'users/registrations/login.html', context={'form': login_form})
    elif request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is None:
            return redirect('login')
        login(request, user)
        return redirect('movies_list')


@login_required
def user_logout(request):
    logout(request)
    return redirect('movies_list')
