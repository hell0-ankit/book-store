from admin_dashboard import views
from django.urls import path


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
   
]
