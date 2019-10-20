from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, Project
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']


class ProjectPostForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['user','design','usability','content']