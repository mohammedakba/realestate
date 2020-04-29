from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.index),
    # path('index', views.index),
    path('home', views.home, name='home'),
    path('about', views.about),
    path('register', views.register),
    path('upload', views.upload),
    # myuploads
    path('myupload', views.myupload),
    # property view
    path('pview', views.pview),

    path('contact', views.contact),
    path('search', views.search),
    path('delete', views.delete),
    path('edit', views.edit),




    # login path
    path('login', auth_views.LoginView.as_view(
        template_name='basics/login.html'), name='login'),

    # logout path
    path('logout', auth_views.LogoutView.as_view(
        template_name='basics/index1.html'), name=''),

    # password reset path
    path('password-reset', auth_views.PasswordResetView.as_view(
        template_name='basics/resetpassword.html'), name='passwrodreset'),

    # password reset done path
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='basics/resetconfirm.html'), name='password_reset_done'),

    # rest comfirm path
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='basics/resetpassword.html'), name='password_reset_confirm'),

    # rest complete
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='basics/resetdone.html'), name='password_reset_complete'),
]
