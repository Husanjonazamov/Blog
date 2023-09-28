from django.contrib.auth import login,authenticate
from django.forms.models import BaseModelForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView
from accounts.forms import UserCreationCustomForm
from .models import User




class SignupView(CreateView):
    form_class = UserCreationCustomForm
    model = User
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


    def form_valid(self, form):
        form.save()
        username = form.data.get("username")
        password = form.data.get("password1")
        user = authenticate(username=username,password=password)

        if not user is None:
            login(self.request,user=user)
            return redirect (reverse("home"))
        else:
            return redirect (reverse("signup"))
        














# Create your views here.
