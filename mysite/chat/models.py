from django.db import models
from django.utils import timezone

# Create your models here.

class Chat_Room(models.Model):
    Title = models.CharField(max_length=50,null=False)

class Chat(models.Model):
    chat_room = models.ForeignKey(Chat_Room,on_delete=models.CASCADE,default='')
    author = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    write_date = models.DateTimeField(auto_now=True)

    


