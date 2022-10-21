from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register, name="register"),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name="logout"),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    
]