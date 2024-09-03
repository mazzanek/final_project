from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('accounts/profile/', profile, name="profile"),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('pbs', views.pb_list, name='pbs'),
    path('add-diving-record/', views.add_diving_record, name='add_diving_record'),
    path('edit-diving-record/<int:record_id>/', views.edit_diving_record, name='edit_diving_record'),
]