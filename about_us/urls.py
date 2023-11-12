from django.urls import path

from about_us import views

urlpatterns = [
    path('about_us', views.About_usTemplateView.as_view(), name='about-us'),
]