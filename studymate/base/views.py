from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

rooms = [
    {
        'name': 'Room buss',
        'description': 'This is room 1 description',
    },
    {
        'name': 'Room 2',
        'description': 'This is room 2 description',
    },
    # Add more rooms here...
]
def home(request): 
    return render(request, 'base/home.html', {'rooms': rooms})
    
def room(request):
    return render(request, 'base/room.html')