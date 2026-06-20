from user import views
from django.urls import path

urlpatterns = [
    path('userprofile/', views.userPofile, name='userprofile'),
   
]

