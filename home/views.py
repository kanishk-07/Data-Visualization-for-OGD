from django.http import HttpResponse
from django.shortcuts import render

def indexHome(request):
    return render(request, 'indexHome.html')