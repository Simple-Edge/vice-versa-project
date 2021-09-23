from django.shortcuts import render
import re

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text= request.GET["usertext"]
    le = user_text.split()
    counter = len(le)
    reversed_text = user_text[::-1]

    return render(request, 'reverse.html',{'usertext':user_text,'reversedtext':reversed_text,'counter':counter})