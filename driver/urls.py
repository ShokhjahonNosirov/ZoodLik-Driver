from django.urls import path
from .views import TaklifView, ProfileView, TaklifDetailView

app_name = 'driver'

urlpatterns = [
    path('taklif', TaklifView.as_view(), name='taklif_list'),
    path('taklif_detail/<int:pk>/', TaklifDetailView.as_view(), name='taklif_detail'),
    path('profile', ProfileView.as_view(), name='profile'),
]