from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
from django.utils.safestring import mark_safe
import json

from .models import Chat_Room
# Create your views here.

# 채팅 방 목록  
def index(request):
    if request.method == "GET":
        chat_rooms = Chat_Room.objects.all()
        context = {'chat_rooms':chat_rooms}
        return render(request,'chat/index.html',context)
    else:
        return render(request,'chat/room.html')

# 채팅
def room(request,room_name):
    return render(request,'chat/room.html',{
        'room_name_json':mark_safe(json.dumps(room_name))
    })
