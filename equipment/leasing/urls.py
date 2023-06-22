from django.urls import path
from .views import SignupPage, LoginPage, HomePage, LogoutPage, AdminLoginPage, AdminPanel

urlpatterns = [
    path('', SignupPage, name='Signup'),
    path('adminlogin', AdminLoginPage, name='adminlogin'),
    path('adminpanel', AdminPanel, name='adminpanel'),
    path('login/', LoginPage, name='login'),
    path('home/', HomePage, name='home'),
    path('logout/', LogoutPage, name='logout'),

]