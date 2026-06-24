from accounts import views
from django.urls import path


urlpatterns = [
    path('login/', views.loginViews, name='login'),
    path('sign-up/', views.signupViews, name='signup'),
    path('logout/', views.logoutView, name='logout'),
    path("forgot-password/",views.forgot_password,name="forgot_password"),
    path("reset-password/<uuid:token>/",views.reset_password,name="reset_password"),
    path('verify-otp/', views.verifyOTPViews, name='verify_otp'),
    path("resend-otp/", views.resend_otp, name="resend_otp"),

    
]
