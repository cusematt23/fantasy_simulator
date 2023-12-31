from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message

#This command tells django you want to be able to work with this model in the admin panel
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
#The user model is registered by default