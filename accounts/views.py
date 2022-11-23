from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import ProfileForm, SignupForm, LoginForm, EditProfileForm


def signup(request):
    if request.method == "GET":
        signup_form = SignupForm()
        return render(request, 'signup.html',
                      context={'form': signup_form})
    elif request.method == "POST":
        signup_form = SignupForm(request.POST)
        if not signup_form.is_valid():
            messages.warning(
                request,
                "This user was created befor!!"
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
        return render(request, 'login.html', context={'form': login_form})
    elif request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is None:
            return redirect('login')
        login(request, user)
        return redirect('movies_list')


def user_logout(request):
    logout(request)
    messages.success(
        request,
        "You're Loged out!"
    )
    return redirect('movies_list')


@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_form = ProfileForm(instance=user)
    return render(request, "accounts/profile.html", context={"user_form": user_form, 'pk': pk})


@login_required
def edit_profile(request, pk, profile=None):
    user = get_object_or_404(User, pk=pk)
    if request.method == "GET":
        user_form = EditProfileForm(instance=user)
        return render(request, 'accounts/edit_profile.html', context={'user_form': user_form, "pk": pk})
    elif request.method == "POST":
        profile_form = EditProfileForm(request.POST, instance=user)
        if not profile_form.is_valid():
            return edit_profile(request, pk, profile_form)
        profile_form.save()
        return redirect('profile', pk)

