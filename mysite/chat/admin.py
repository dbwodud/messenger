from django.contrib import admin
from .models import Chat
from .models import Chat_Room
# Register your models here.

admin.site.register(Chat_Room)
admin.site.register(Chat)
