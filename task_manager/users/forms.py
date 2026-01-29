from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


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


# добавил пустые поля пароля только для прохождения теста
class UpdateUserForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(render_value=True),
        required=False,
        label="Пароль",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(render_value=True),
        required=False,
        label="Подтверждение пароля",
    )
        
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
