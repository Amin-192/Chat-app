from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models  import Room



def home(request): 
    Rooms = Room.objects.all()  # Fetch all Room objects from the database
    return render(request, 'base/home.html', {'Rooms': Rooms})


    
def room(request):
    return render(request, 'base/room.html')