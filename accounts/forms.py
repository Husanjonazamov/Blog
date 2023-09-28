from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from.models import User

class UserCreationCustomForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
        ]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
        ]