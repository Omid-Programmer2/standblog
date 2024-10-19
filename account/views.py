# from django.contrib.auth.models import User
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
        return redirect('/')

    if request.method == 'POST':
        # print(request.POST.get('username'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # print(user)
        # print(user.first_name)
        if user is not None:
            login(request, user)
            return redirect('/')
    # print(type(render(request, 'account/login.html', {})))
    return render(request, 'account/login.html', {})

#HttpRequest
#HttpResponse


def user_register(request):
    return render(request, "account/register.html", {})
def user_logout(request):
    logout(request)
    return redirect('/')
