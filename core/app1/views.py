from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the app1 index.") 

def sum(request):
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    c = a + b
    return HttpResponse(f"The sum of {a} and {b} is {c}")

def user(request, user_id):
    users = {
        1: "Alice",
        2: "Bob",
        3: "Charlie",

    }

    if user_id in users:
        return HttpResponse(f"Hello, {users[user_id]}!")
    
    return HttpResponse(f"User not found.", status=404)

