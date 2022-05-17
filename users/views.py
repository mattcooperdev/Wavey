from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm

def home(request):


def register(request):
    form = UserChangeForm()
    return render(request, 'users/register.html', {'form': form})
