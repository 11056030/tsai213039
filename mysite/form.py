from django import forms
from .models import User
 
 
# creating a form
class UsersForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = User
 
        # specify fields to be used
        fields = [
            "name",
            "email",
            "password",
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }