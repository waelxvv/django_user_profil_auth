from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    DateDeNaissance = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    Telephone = forms.IntegerField()
    Adresse = forms.CharField()
    class Meta:
        model = User
        fields = ('username','email', 'DateDeNaissance','Telephone','Adresse', 'password1', 'password2', )
