from typing import Any, Optional
from django.db import models
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Thread, Message
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView): #Todos los hilos del usuario
    template_name = "messenger/thread_list.html"

    """model = Thread

    def get_queryset(self):
        queryset = super(ThreadList, self).get_queryset()
        return queryset.filter(users=self.request.user) #Filtrar todos los hilos del usuario identificado en el momento
        No hace falta, ya que en el template se pueden consultar los hilos del usuario, de forma directa.
        //user.threads.all()
        """

@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView): #Unica instancia con todos los mensajes del thread
    model = Thread

    #Para que el usuario solo pueda ver los hilos de los que forma parte
    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj #Mostrar desde el template todos los mensajes que forman parte de el
    
def add_message(request, pk):
    json_response = {'created':False} #Cuando se agregue un mensaje, se devolvera una respuesta json_response
    if request.user.is_authenticated:
        content = request.GET.get('content', None) #Recupera el contenido del diccionario de parameros GET, y si no existe None
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
            if len(thread.messages.all()) is 1:
                json_response['first'] = True
    else:
        raise Http404("El usuario no esta identificado")

    return JsonResponse(json_response)

@login_required
#Vista normal, no se necesita agregar el adorno al metodo
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))