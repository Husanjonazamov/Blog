from django.contrib import admin
from .models import User
from .forms import CustomUserChangeForm,UserCreationCustomForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationCustomForm
    form = CustomUserChangeForm
    model = User

admin.site.register(User, CustomUserAdmin)
# Register your models here.
