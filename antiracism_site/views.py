from django.shortcuts import render
from django.http import HttpResponse

def testfunction(request):
    return HttpResponse("<h1>It worked! Again!</h1>")
