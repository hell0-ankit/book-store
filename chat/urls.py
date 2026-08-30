from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("", views.customer_chat_view, name="customer_chat"),
    path("send/", views.send_message, name="send_message"),
    path("get/", views.get_messages, name="get_messages"),
    path("admin-support/", views.admin_chat_dashboard, name="admin_chat"),
    path("admin-unread-counts/", views.get_admin_unread_counts, name="admin_unread_counts"),
]