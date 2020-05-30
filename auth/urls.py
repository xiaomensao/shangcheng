from django.urls import path, include
from auth import views

urlpatterns = [
    path('signup/', views.signup),
    path('', include('django.contrib.auth.urls')),
]