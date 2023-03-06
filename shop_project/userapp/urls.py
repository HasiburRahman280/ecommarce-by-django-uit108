from django.urls import path
from .views import register,profile_func,profile_update_func
from django.contrib.auth import views as auth_views
urlpatterns = [
    path ('register', register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='userapp/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='userapp/logout.html'), name='logout'),
    path('user/profile', profile_func, name='user-profile'),
    path('user/profile/update',profile_update_func , name='profile-update'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='userapp/password-change.html'), name='password-change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='userapp/password_change_done.html'), name='password_change_done')


]