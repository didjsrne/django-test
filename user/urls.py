from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.sign_up_view, name='signup'),
    path('login/', views.login_view, name='login'),

 ] 
