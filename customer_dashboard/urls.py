from customer_dashboard import views
from django.urls import path

urlpatterns = [
    path('', views.customerDashboard, name='customer_dashboard'),
    path('cm_orders_history/', views.cmOrdersHistory, name='cm_orders_history'),
    path('cm_personal_details/', views.cmPersonalDetails, name='cm_personal_details'),
    path('cm_update_personaldetail/', views.cmPersonalDetailsForm, name="cm_update_personaldetail")
]

