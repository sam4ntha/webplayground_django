#from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

class StaffRequiredMixin(object):
    """Este mixin requerira que el usuario sea miembro del Staff
    Esta es una clase que reimplementa el metodo dispatch
    """

    def dispatch(self, request, *args, **kwargs):
        #print(request.user) Se ha modificado el comportamiento de dispatch
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs) #Devuelve lo que debe regresar dispatch

# Create your views here.
class PageListView(ListView):
    model = Page
    """pages = get_list_or_404(Page)
    return render(request, 'pages/pages.html', {'pages':pages})"""

class PageDetailView(DetailView):
    model = Page
    """page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page.html', {'page':page})"""

class PageCreate(StaffRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    #fields = ['title', 'content', 'order'] Se omite porque ya está incluido en el forms
    success_url = reverse_lazy('pages:pages')
    """def get_success_url(self):
        return reverse('pages:pages')"""
    
class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
   
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
    
class PageDelete(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')