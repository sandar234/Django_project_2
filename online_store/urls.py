"""
URL configuration for online_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from userextend.forms import AuthenticationNewForm, NewPasswordChangeForm, \
    NewPasswordResetForm, NewSetPasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm),
         name="login"),
    path("password_change/",
         views.PasswordChangeView.as_view(form_class=NewPasswordChangeForm),
         name="password_change"),
    path("password_reset/",
         views.PasswordResetView.as_view(form_class=NewPasswordResetForm),
         name="password_reset"),
    path("reset/<uidb64>/<token>/",
         views.PasswordResetConfirmView.as_view(form_class=NewSetPasswordForm),
         name="password_reset_confirm"),
    path('', include('django.contrib.auth.urls')),
    path('', include('userextend.urls')),
    path('', include('category.urls')),
    path('', include('product.urls')),
    path('', include('order.urls')),
    path('', include('about_us.urls')),
    path('', include('shop_finder.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
