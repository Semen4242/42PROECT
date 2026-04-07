from django import forms
from .models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["login","password","first_name","last_name","age"]
        labels = {
            "login": "Логин",
            "password": "пароль",
            "first_name": "имя",
            "last_name": "фамилия",
            "age": "возраст",
        }