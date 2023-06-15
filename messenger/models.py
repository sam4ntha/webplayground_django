from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.
class Message(models.Model):  #Almacena los mensajes
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['created']


class Thread(models.Model): #Hilo de conversación
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
    #Punto de encuentro que almacena los usuarios y los mensajes que escriben estos

def messages_changed(sender, **kwargs):
    instance = kwargs.pop("instance", None)
    #Recupera el hilo al que se estan mandando/agregando los mensajes
    action =  kwargs.pop("action", None)
    #Acción que se ejecuta (preadd antes de agregar mensajes/postadd momentos después de agregarlos)
    pk_set = kwargs.pop("pk_set", None)
    #Conjunto que almacena los identificadores de todos los mensajes que se van a añadir en esta relación ManyToMany, conjunto como lista pero no se pueden duplicar elementos
    print(instance, action, pk_set)

    false_pk_set = set()
    if action is "pre_add": 
        for msg_pk in pk_set: #Comprueba todos los mensajes pk que hay en el conjunto pk_set(lista)
            msg = Message.objects.get(pk=msg_pk) #Se recuperan los mensajes
            if msg.user not in instance.users.all(): #si el autor del mensaje no se encuentra en la instancia  del hilo mostrara un debug
                print("Lo sentimos, ({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk)


    #Buscar los mensajes de false_pk_set sí están en pk_set y los borramos de pk_set
    pk_set.difference_update(false_pk_set)#Elimina el 3 que esta en false_pk_set y quedan los mensajes 1 y 2 de los 2 usuarios de la instancia

m2m_changed.connect(messages_changed, sender=Thread.messages.through) #Conectando señal con cualquier cambio que suceda en ManyToMany Messages