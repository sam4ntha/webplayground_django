from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y tambien debe ser válido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):  #Validar el campo que se desea
        email = self.cleaned_data.get("email") #Recuperar el valor que tiene cleaned, al momento de enviar el formulario
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ya ha sido registrado, prueba con otro.") 
        return email
        #Se manda un error si ya existe el email ingresado
         #Comprobar si existe en la base de datos, filter nunca da error, devuelve una lista vacia o un query set si no llega a haber algun elemento

         #Se ha definido un metodo para validar el email ingresado para registrarse, se recupera el email que se ha enviado en el formulario, cmprueba si existe algun usuario con el email que se ha recibido. Si existe, significa que se ha registrado y se regresa un error de validacion devolviendo un mensaje.
         #En caso de que no este en la base de datos, devuelve el email dando a entender que ha ido validado 