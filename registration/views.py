from .forms import UserCreationFormWithEmail
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

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