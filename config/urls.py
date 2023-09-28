
from django.contrib import admin
from django.urls import path,include,re_path
from home.views import HomePage,BlogDetailView
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include("django.contrib.auth.urls")),
    path("accounts/",include("accounts.urls")),
    path("",include("home.urls")),
    re_path(r"media/(.*)",serve, {"document_root":settings.MEDIA_ROOT})

]
