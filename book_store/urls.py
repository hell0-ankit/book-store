from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

# 1. View function yahan define karein:
def custom_404_view(request, exception=None):
    return render(request, "404.html", status=404)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('product/', include('product.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('customer_dashboard/', include('customer_dashboard.urls')),
    path("chat/", include("chat.urls")),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
handler404 = custom_404_view