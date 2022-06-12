from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import (UserRegisterForm,
                    UserUpdateForm,
                    UserDeleteForm,
                    ProfileForm)
from .models import Profile


def register(request):
    '''
    View for registering new User
    '''
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
        # User form containing username and email
        user_form = UserUpdateForm(request.POST, instance=request.user)
        # Profile form containing Profile model fields
        profile_form = ProfileForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated')
            return redirect('profile')
    else:
        # get an instance of the Profile and the User
        profile = get_object_or_404(Profile, user=request.user)
        user = get_object_or_404(User, username=request.user.username)
        # User form containing username and email
        user_form = UserUpdateForm(instance=user)
        # Profile form containing Profile model fields
        profile_form = ProfileForm(instance=profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
    return render(request, 'users/edit_profile.html', context)


@login_required
def deleteProfile(request):
    '''
    View to delete profile after confirming email address
    '''
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = UserDeleteForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('email') == profile.user.email:
                user = request.user
                logout(request)
                user.delete()
                messages.success(request, 'Account deleted!')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Incorrect email entered!')
    else:
        form = UserDeleteForm()
        context = {'form': form}
        return render(request, 'users/delete_profile.html', context)
