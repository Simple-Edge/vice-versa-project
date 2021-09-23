from django.shortcuts import render

def home(reguest):
    return render(reguest, 'home.html')