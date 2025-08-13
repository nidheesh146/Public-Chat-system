# filepath: /C:/Users/NIDHEESH/Desktop/Altos Work/chatbotproject/chatbotapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('enter/',views.enter,name='enter'),
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/<str:room>/', views.get_messages, name='get_messages'),
     path('company_login/', views.company_login, name='company_login'),
    path('unemployed_login/', views.unemployed_login, name='unemployed_login'),
    path('company_registration/', views.company_registration, name='company_registration'),
    path('unemployed_registration/', views.unemployed_registration, name='unemployed_registration'),
    path('admindash/', views.admindash, name='admindash'),
    path('emp_dashboard/',views.emp_dashboard,name='emp_dashboard'),
    path('chat_unemp/',views.chat_unemp,name='chat_unemp'),
    path('enter_unemp/',views.enter_unemp,name='enter_unemp'),



 ]