from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import translation
# from django.contrib.auth.forms import UserCreationForm

import json
import datetime

from . import forms
from . import models
from microfeed.models import EventPostTime
from feed import functions
from feed.functions import UPLOADS_DIR

def set_english(request):
    user_language = 'en-us'
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def set_japanese(request):
    user_language = 'ja'
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def home(request):
    context = {}
    if not request.session.get(translation.LANGUAGE_SESSION_KEY):
        user_language = 'ja'
        request.session[translation.LANGUAGE_SESSION_KEY] = user_language
        translation.activate(user_language)
    context['upcoming_events'] = functions.get_upcoming_events()
    return render(request, 'main/home.html', context)

def login_view(request):
    context = {}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print('it ran')
        if user is not None:
            print('user is not none')
            if user.is_active:
                print('user is active')
                login(request, user)
                # redirect_to = request.POST.get(redirect_field_name, request.GET.get(redirect_field_name, ''))  
                return redirect('home')
            else:
                # Return a 'disabled account' error message
                context['login_error'] = 'Your account has a problem.  Please contact the administrator.'
                return render(request, 'main/login.html', context)
        else:
            # Return an 'invalid login' error message.
            context['login_error'] = 'Login failed.  Please reenter your username and password.'
            return render(request, 'main/login.html', context)
    return render(request, 'main/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def create_account(request):
    context = {}
    fUser = forms.UserCreationForm()
    if request.method == 'POST':
        fUser = forms.UserCreationForm(request.POST)
        if fUser.is_valid():
            oUser = fUser.save(commit=False)
            oUser.save()
            image = fUser.cleaned_data['image']
            if image:
                imageArr = image.split(',')
                file_name = 'image_' + str(oUser.id) + '.png'
                fh = open(UPLOADS_DIR + "user_images/" + file_name, "wb")
                fh.write(imageArr[1].decode('base64'))
                fh.close()
                oProfile = models.Profile(user=oUser, image_name=file_name, username2=fUser.cleaned_data['username2'])
                oProfile.save()
            else:
                oProfile = models.Profile(user=oUser, username2=fUser.cleaned_data['username2'])
                oProfile.save()
            #login user and redirect
            login(request, oUser)
            return redirect('home')
    context['fUser'] = fUser
    return render(request, 'main/create_account.html', context)

@login_required
def edit_account(request):
    context = {}
    fUser = forms.UserChangeForm(instance=request.user)
    if request.method == 'POST':
        fUser = forms.UserChangeForm(request.POST, instance=request.user)
        if fUser.is_valid():
            oUser = fUser.save()
            # oUser.save()
            image = fUser.cleaned_data['image']
            if image:
                imageArr = image.split(',')
                file_name = 'image_' + str(oUser.id) + '.png'
                fh = open(UPLOADS_DIR + "user_images/" + file_name, "wb")
                fh.write(imageArr[1].decode('base64'))
                fh.close()
                oProfile, created = models.Profile.objects.get_or_create(user=oUser)
                oProfile.image_name = file_name
                oProfile.username2 = fUser.cleaned_data['username2']
                oProfile.save()
            else:
                oProfile, created = models.Profile.objects.get_or_create(user=oUser)
                oProfile.username2 = fUser.cleaned_data['username2']
                oProfile.save()
            #login user and redirect
            return redirect('home')
    context['fUser'] = fUser
    return render(request, 'main/edit_account.html', context)













