from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page 
        fields = ['title', 'content', 'order'] 
        #Indicar que campos queremos permitirle al usuario editar en el formulario
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'0den'}),
        }
        labels = {
            'title': '', 'content': '', 'order': ''
        }

