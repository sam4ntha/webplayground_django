from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile

#Create your views here

class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 3

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'    
    #Una DetailView por defecto toma una pk o una slug para recuperar la instancia, pero debemos recuperar el perfil a partir del nombre de usuario.

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
    #Para recuperar el perfil a partir del parámetro <username> del path, se debe sobreescribir su método get_object