from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.show_profile, name='profile'),
    path('changepwd/', views.change_pwd, name='changepwd'),
]
