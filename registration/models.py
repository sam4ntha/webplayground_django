from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver #Llamar automaticamente
from django.db.models.signals import post_save

#Optimizando almacenamiento con el avatar
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    #OneToOneField solo puede haber un perfil por usuario
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']
        #Manejar paginación

@receiver(post_save, sender=User) #Después de guardarla
def ensure_profile_exists(sender, instance, **kwargs): 
    #Signal encargada de comprobar si el perfil siempre existe
    if kwargs.get('created', False): #Devuelve falso s no existe la entrada en el diccionario
        Profile.objects.get_or_create(user=instance) #Si la insancia se acaba de crear, entra aqui y se crea e perfil.
        #print("Se acaba de crear un usuario y un perfil enlazado.")
#Señal, función que ejecuta un código en un momento determinado en la vida de una instancia, ya sea antes de guardarla, después o antes de borrarla o después.