from django.urls import path
from sentryapp import views


urlpatterns = [
    path('', views.home, name='home')
]