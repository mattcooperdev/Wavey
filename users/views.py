from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created! You can now login.')
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
    profile = get_object_or_404(Profile, user=request.user)
    if request.user == profile.user:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                try:
                    form.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request, f'Profile for {profile.username} updated')
                    return redirect('profile')
                except:
                    messages.error(request, 'ERROR: Only image file types are allowed')
                    context = {'form': form}
                    return render(request, 'users/edit_profile.html', context)
        else:
            form = ProfileForm(instance=request.user.profile)
    else:
        id = request.user.id
        return redirect('profile', id)

    context = {'form': form}
    return render(request, 'users/edit_profile.html', context)
