from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    #success_url = reverse_lazy('login') se pasa a la definicion para concatenar un mensaje de registro
    template_name = 'registration/signup.html'
    """En lugar de crear un formulario desde cero, se importará uno genérico, pasándoselo a la vista CreateView para que lo maneje todo automáticamente."""

    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        #Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder': 'Correo electrónico'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Confirmar contraseña'})

        return form
    #Devuelve el formulario

    """Se esta extendiendo el formulario UserCreationForm, este tiene sus propias validaciones, no se puede sobreescribir en un campo widget, ya que se borran sus validaciones y configuraciones que ya tiene.
    Se tendria que modificar las validaciones en tiempo real(parte superior get_form)."""


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    template_name = 'registration/profile_form.html'
    success_url = reverse_lazy('profile')
    """Solo disponible para un usuario autenticado y pueda actualizar su perfil"""    

    def get_object(self):
        #Recuperar el objeto que se va a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    #get_or_create busca a partir del filtro que se le proporciona, si no lo encuentra lo crea.
    #No se puede recuperarlo ni devolverlo directamente, pq al devolverlo directamente regresa una tupla formada por el propio objeto que se esta recuperando o editando(Profile)

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    template_name = 'registration/profile_email_form.html'
    success_url = reverse_lazy('profile')    

    def get_object(self):
        #Recuperar el objeto que se va a editar
        return self.request.user
    
    def get_form(self, form_class=None):
        #Sobreescirbir en tiempo de ejecucionn pq User(modeloUsuario) ya tiene sus propios validadores y sus propios widgets
        form = super(EmailUpdate, self).get_form()
        #Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder': 'Correo electrónico'})
        return form