from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.models import User


def userProfiles(request):
    profiles = UserProfile.objects.all()
    last_active = User.objects.all().last().last_login
    print(last_active)
    context = {'profiles': profiles, 'last_active': last_active}
    return render(request, "users/user_profiles.html", context)


def singleUser(request, pk):
    profile = UserProfile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, "users/single_user.html", context)
