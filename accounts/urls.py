from django.urls import path
from accounts import views
#from django.contrib.auth.views import (password_reset, password_reset_done,
 #                                       password_reset_confirm, password_reset_complete)




#Template Tagging
app_name = 'accounts'

urlpatterns = [

    path('login/', views.user_login,  name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/siwes/', views.edit_details, name='edit_details'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),

    #path('reset-password/', password_reset,{'template_name':
    #'accounts/reset_password.html', 'post_reset_redirect':
    #'accounts:password_reset_done', 'email_template_name':
    #'accounts/reset_password_email.html'}, name='reset_password'),


    #path('reset_password-password/done/',  password_reset_done, {'template_name':
    #'accounts/reset_done.html'}, name='password_reset_done'),

    #path('reset_password-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',  password_reset_confirm, {'template_name':
    #'accounts/reset_confirm.html', 'post_reset_redirect':
    #'accounts:password_reset_complete'}, name='password_reset_confirm'),


    #path('reset-password/complete/',  password_reset_complete, {'template_name':
    #'accounts/reset_complete.html'}, name='password_reset_complete'),

]
