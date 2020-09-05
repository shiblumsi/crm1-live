from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [
    path('signup',views.signup,name='register'),
    path('login',views.login_,name='login'),
    path('logout',views.logout_,name='logout'),
    path('',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('user',views.user_,name='user'),
    path('products',views.products,name='product'),
    path('customer/<int:pk>',views.customer,name='customer'),
    path('createorder',views.createorder,name='createorder'),
    path('updateorder/<int:pk>',views.updateorder,name='updateorder'),
    path('deleteorder/<int:pk>',views.deleteorder,name='deleteorder'),
    path('addproduct',views.addproduct,name='addproduct'),


    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
        name="password_reset_complete"),



]
