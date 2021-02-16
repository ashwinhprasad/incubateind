
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserModel

class CreateCustomUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email','name','phone_no','password1','password2')
