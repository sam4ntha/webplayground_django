from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.
# def home(request):
#return render(request, "core/home.html")
class HomePageView(TemplateView):
    template_name = "core/home.html"

    #Devolviendo diccionario de contexto
    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Pensando de que hacer la web"
        return context"""
    
    #Devolciendo render, procesando la respuesta de la vista, sobreescribiendola en si misma
    #Cuando se esten sobreescribiendo metodos dentro de una vista basada en clases, se estaran pasandoles argumentos o argumentos clave valor y/o ambos
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Pensando'})


class ResumePageView(TemplateView):
    template_name = "core/resume.html"

class ContactPageView(TemplateView):
    template_name = "core/contact.html"

class ProjectsPageView(TemplateView):
    template_name = "core/projects.html"