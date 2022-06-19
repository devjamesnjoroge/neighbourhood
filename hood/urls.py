from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('auth/register/', views.register, name='register'),
    path('auth/login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(template_name='authentication/logout.html'), name='logout'),
    path('neighbourhoods/', views.search_hood, name='neighbourhoods'),
    path('neighbourhoods/create/', views.create_hood, name='create_hood'),
    path('neighbourhoods/<int:hood_id>/', views.hood_profile, name='hood_profile'),
]