from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models  import Room , User




def home(request): 
    Rooms = Room.objects.all()  # Fetch all Room objects from the database
    Users = User.objects.all()  # Fetch all User objects from the database
    context = {
        'Rooms': Rooms,
        'Users': Users,
    }
    return render(request, 'base/home.html', context)


    
def room(request):
    return render(request, 'base/room.html')