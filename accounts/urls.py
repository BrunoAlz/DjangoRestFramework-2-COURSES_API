from django.urls import path
from accounts import views
from accounts import views as accounts_view


app_name = 'accounts'

urlpatterns = [

    path('login', accounts_view.user_login, name='login'),
    path('logout', accounts_view.user_logout, name='logout'),
    path('register', accounts_view.user_register, name='register'),


    path('forgot-password', views.forgot_password, name='forgot-password'),
    path('confirm-email', views.confirm_email, name='confirm-email'),
    path('reset-password', views.reset_password, name='reset-password'),
    path('lock-screen', views.lock_screen, name='lock-screen'),

]