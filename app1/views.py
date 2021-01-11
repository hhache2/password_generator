from django.shortcuts import render
import random
from .passwordGenerator import getPassword

# Create your views here.

def home(request):
    return render(request, 'app1/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', '11'))
    isUpperCase = request.GET.get('uppercase')
    isSpecial = request.GET.get('special')
    isNumbers = request.GET.get('numbers')

    thePassword = getPassword(length, isUpperCase, isNumbers, isSpecial)

    return render(request, 'app1/password.html', {'password': thePassword})

def about(request):
    return render(request, 'app1/about.html')