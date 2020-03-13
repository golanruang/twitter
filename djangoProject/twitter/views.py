from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User, Post
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate
from .forms import NameForm, PasswordForm
def authenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    # if user details entered are a valid user's
    for user in User.objects.all():
        if user.username == username and user.password == password:
            context = {
                'Username':user.username,
                'Password':user.password,
                'First Name':user.firstName,
                'Last Name':user.lastName,
                'Email Address':user.emailAddress,
                'User Id':user.userId,
            }
            return HttpResponseRedirect('login/')
    return render(request, 'twitter/twitterLogin.html', {'name': name,'password':password})

def twitterPosts(request):
    # stuff to give to html page twitterPosts.html
    latest_post_list = Post.objects.all()
    #order_by('dateCreated')[:10]
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'twitter/twitterPosts.html', context)

def twitterLogin(request):
    # stuff to give to html page twitterLogin.html
    context = {}

    return render(request, 'twitter/twitterLogin.html', context)
