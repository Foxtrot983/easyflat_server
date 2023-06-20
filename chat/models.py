from django.db import models
from django.contrib.auth import get_user_model

from houses.models import House

class Chat(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='chat_user')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="chat_house")

class Message(models.Model):
    pass