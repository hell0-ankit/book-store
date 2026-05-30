from accounts import views
from django.urls import path


urlpatterns = [
    path('login/', views.loginViews, name='login'),
    
]
