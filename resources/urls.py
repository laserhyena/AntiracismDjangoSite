from django.urls import path
from .views import resource_list

urlpatterns = [
    path('', resource_list),
]
