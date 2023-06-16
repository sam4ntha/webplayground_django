from typing import Any, Optional
from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Thread
from django.http import Http404

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