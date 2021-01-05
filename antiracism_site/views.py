from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    # return HttpResponse("<h1>This is the homepage for my anti-racism project!</h1>")
    return render(request, 'homepage.html')


def about(request):
    # return HttpResponse("This project will dynamically provide resources to further one's efforts to be anti-racist.")
    return render(request, 'about.html')
