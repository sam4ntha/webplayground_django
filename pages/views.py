#from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse, reverse_lazy
from .models import Page
from .forms import PageForm

# Create your views here.
class PageListView(ListView):
    model = Page
    """pages = get_list_or_404(Page)
    return render(request, 'pages/pages.html', {'pages':pages})"""

class PageDetailView(DetailView):
    model = Page
    """page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page.html', {'page':page})"""

class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    #fields = ['title', 'content', 'order'] Se omite porque ya está incluido en el forms
    success_url = reverse_lazy('pages:pages')
    """def get_success_url(self):
        return reverse('pages:pages')"""
    
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
   
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
    
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')