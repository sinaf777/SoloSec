from django.shortcuts import render, get_object_or_404
from .models import Room

# Create your views here.

def room_list(request):
    rooms = Room.objects.all()
    return render(request, "rooms/room_list.html", {"rooms": rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, "rooms/room_detail.html", {"room": room})
