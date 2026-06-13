from accounts import views
from django.urls import path


urlpatterns = [
    path('login/', views.loginViews, name='login'),
    path('sign-up/', views.signupViews, name='signup'),
    
]
