from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib import messages


def login(request):
    if request.session.has_key('uid'):
        context = {'username': request.session['uid']}
        return render(request, 'accounts/services.html', context)
    if request.method == 'POST':
        curr_user = Accounts.objects.all().filter(pk=request.POST["username"], password=request.POST["password"])
        if curr_user.count() == 1:
            request.session['uid'] = request.POST["username"]
            context = {'username': request.session['uid']}
            return render(request, 'accounts/services.html', context)
        else:
            messages.info(request, "invalid")
    context = {}
    return render(request, 'accounts/login.html', context)


def register(request):
    if request.session.has_key('uid'):
        del request.session['uid']
    if request.method == 'POST':
        if request.POST["pass1"] == request.POST["pass2"]:
            account_form = Accounts()
            account_form.user_name = request.POST["username"]
            account_form.email = request.POST["email"]
            account_form.phone_num = request.POST["phone_num"]
            account_form.password = request.POST["pass1"]
            account_form.save()
            return render(request, 'accounts/login.html')
        else:
            return HttpResponse("password dosen't match")

    context = {}
    return render(request, 'accounts/register.html', context)


def forgotPassword(request):
    context = {}
    return render(request, 'accounts/forgotPassword.html', context)


def updatePassword(request):
    if request.method == 'POST':
        context = {}
        return render(request, 'accounts/updatePassword.html', context)
    return forgotPassword(request)


def logout(request):
    del request.session['uid']
    return redirect('login')


def contact(request):

    context = {'username': request.session['uid']}
    return render(request, 'accounts/contact.html', context)


def profile(request):

    if request.method == 'POST':
        account = Accounts()
        account = Accounts.objects.filter(user_name=request.session['uid'])[0]

    account = Accounts.objects.filter(user_name=request.session['uid'])
    context = {'account': account[0], 'username': request.session['uid']}
    return render(request, 'accounts/profile.html', context)


def about(request):
    context = {'username': request.session['uid']}
    return render(request, 'accounts/about.html', context)