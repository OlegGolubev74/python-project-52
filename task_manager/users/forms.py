from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        )

'''
class UpdateUserForm(MyUserCreationForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            username = self.cleaned_data['username']
        return username
'''

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

