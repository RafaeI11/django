# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User 
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]

# forms.py
from django import forms

class CompraForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1, label='Cantidad a comprar')
    # Puedes agregar más campos según tus necesidades (dirección de envío, etc.)
