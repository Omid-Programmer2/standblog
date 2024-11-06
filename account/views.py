# from django.contrib.auth.models import User
from lib2to3.fixes.fix_input import context

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
# User

def user_login(request):
    # print(type(request))
    # print(request.user.first_name)
    # print(request.user.is_authenticated)
    # print(request.user.username)
    # print(request.user.is_anonymous)

    # user = request.user
    # print(user.is_anonymous)
    # print(user.first_name)

    # if request.user.is_authenticated:
    #     pass

    # request.user.first_name = 'reza'
    # request.user.save()

    # request.user
    # user = User.objects.get(username="omid")

    if request.user.is_authenticated:
        # return redirect('/')
        return redirect('home_app:home')

    if request.method == 'POST':
        # # print(request.POST.get('username'))
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
        # # print(user)
        # # print(user.first_name)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home_app:home')
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])
            login (request, user)
            # sms = request.
            return redirect('home_app:home')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})



    # print(type(render(request, 'account/login.html', {})))
    return render(request, 'account/login.html', {})

#HttpRequest
#HttpResponse


def user_register(request):
    context = {'errors':[]}
    if request.user.is_authenticated:
        return redirect('home_app:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['errors'].append("passwords art not same")
            return render(request, 'account/register.html', context)

        # if User.objects.get(username=username):
        #     context['errors'].append("this username is exists")
        #     return render(request, 'account/register.html', context)

        user = User.objects.create_user(username=username, password=password1, email=email)
        login(request, user)
        return redirect('home_app:home')

    return render(request, "account/register.html", {})
def user_logout(request):
    logout(request)
    return redirect('home_app:home')
