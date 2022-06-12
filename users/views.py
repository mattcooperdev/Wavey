from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileForm
from .models import Profile
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Account for {username} has been created! \
                                  You can now login.')
            return redirect('account_login')
    else:
        form = UserRegisterForm()
    return render(
        request,
        'users/register.html',
        {
            'form': form},
        )


@login_required
def profile(request):
    return render(
        request,
        'users/profile.html',
        {
            'profile': profile},
        )


@login_required
def editProfile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated')
            return redirect('profile')
    else:
        profile = get_object_or_404(Profile, user=request.user)
        user = get_object_or_404(User, username=request.user.username)
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileForm(instance=profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
    return render(request, 'users/edit_profile.html', context)
