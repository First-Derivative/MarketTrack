from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import UserAccount

class RegisterForm(UserCreationForm):
  class Meta:
    model = UserAccount
    fields = ("username", "email" , "password1", "password2")

  username = forms.CharField(max_length=30, help_text="This is what you'll use to login",widget=forms.TextInput(attrs={
  "placeholder": "RockstarJeans3500",
  "class": "form-control std_input",
  "id": "register_username",
  }))

  email = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={
  "placeholder": "jacque@webster.com",
  "class": "form-control std_input",
  "id": "register_email",
  }))

  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
  "placeholder": "Password",
  "class": "form-control std_input",
  "id": "register_pass1",
  }))

  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
  "placeholder": "Confirm Password",
  "class": "form-control std_input",
  "id": "register_pass2",
  }))


  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["password1"].label = "Password"
    self.fields["password2"].label = "Re-Enter Password"


class LoginForm(ModelForm):

  class Meta:
    model = UserAccount
    fields = ("username", "password")

  username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
    "class": "form-control std_input",
    "id": "login_username",
  }))

  password = forms.CharField(widget=forms.PasswordInput(attrs={
    "class": "form-control std_input",
    "id": "login_password",
  }))


  # minor login validation 
  def clean(self):
    username = self.cleaned_data["username"]
    password = self.cleaned_data["password"]
    if not authenticate(username=username, password=password):
      raise forms.ValidationError("Incorrect Credentials")


