from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from .models import Player
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PlayerSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def Signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        height = request.POST.get('height')
        email = request.POST.get('email')
        password = request.POST.get('password')
        pwd2 = request.POST.get('pwd2')


        if password != pwd2:
            return HttpResponse('Password did not match')

        else:
            user = User.objects.create_user(username=name, email=email, password=password)
            Player.objects.create(user=user, name=name, age=age, height=height, email=email, password=password)
            return HttpResponse('Signup success')


def Login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponse('You are already logged in')
        else:
            return render(request, 'login.html')
    else:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            hashed_pass = make_password(password)
            user = User.objects.get(username=username)
            if user is not None:
                if authenticate(request, username=username, password=password):
                    login(request, user)
                    return HttpResponse(f'Logged in as {user}')
            else:
                return HttpResponse('User not found')
        except ObjectDoesNotExist:
            return HttpResponse('User not found')


def Logout(request):
    logout(request)
    return HttpResponse('Logged out successfully')

class CaptainHomeView(viewsets.ModelViewSet):
    queryset = Player.objects.filter(is_captain=False)
    serializer_class = PlayerSerializer

