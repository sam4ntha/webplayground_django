from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):  #Almacena los mensajes
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['created']


class Thread(models.Model): #Hilo de conversacion
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
    #Punto de encuentro que almacena los usuarios y los mensajes que escriben estos