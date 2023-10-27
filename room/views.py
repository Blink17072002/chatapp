from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

from .models import Room, Message
from .forms import RoomForm

# Create your views here.
def rooms(request):
    rooms = Room.objects.all()

    context = {'rooms': rooms}
    return render(request, 'room/rooms.html', context)


def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room:rooms')  # Redirect to a page displaying all rooms
    else:
        form = RoomForm()
    
    context = {'form': form}
    return render(request, 'room/create_room.html', context)


def room_messages(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    user = request.user
    # Get the current user's avatar URL
    avatar_url = settings.STATIC_URL + "images/avatar.svg"

    context = {
        'room': room,
        'messages': messages,
        'user': user,
        'avatar_url': avatar_url,  # Pass the sender's avatar URL
    }
    return render(request, 'room/room_messages.html', context)
   