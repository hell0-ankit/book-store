from accounts import views
from django.urls import path


urlpatterns = [
    path('login/', views.loginViews, name='login'),
    path('sign-up/', views.signupViews, name='signup'),
    path('forget-passward/', views.forgetViews, name='forgetpassward'),
    path('verify-otp/', views.verifyOTPViews, name='verify_otp'),
    path("resend-otp/", views.resend_otp, name="resend_otp"),
    path("reset-password/", views.reset_password, name="reset_password"),
    
]
