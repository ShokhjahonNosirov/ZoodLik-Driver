from django.urls import path
from .views import TaklifView, ProfileView

app_name = 'driver'

urlpatterns = [
    path('taklif', TaklifView.as_view(), name='taklif'),
    path('profile', ProfileView.as_view(), name='profile'),
]