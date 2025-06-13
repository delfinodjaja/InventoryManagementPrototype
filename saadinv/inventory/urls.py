from django.contrib import admin
from django.urls import path
from .views import Index,SignUpView,Dashboard,inventory,create_appointment
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', Index.as_view(),name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/',auth_view.LoginView.as_view(template_name='inventory/login.html'),name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),
    path('dashboard/',Dashboard.as_view(),name='dashboard'),
    path('inventory/', inventory.as_view(), name='inventory'),
    path('book_cosultation/', create_appointment.as_view(), name='book')
]