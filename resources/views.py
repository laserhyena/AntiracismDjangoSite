from django.shortcuts import render
from .models import Resource

# Create your views here.
def resource_list(request):
    categories = Resource.CATEGORIES
    resources = {category[1] : Resource.objects.filter(category=category[0]) for category in categories}
    return render(request, 'resources/resource_list.html', context={"resources": resources})
