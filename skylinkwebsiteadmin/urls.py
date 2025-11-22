from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 🔥 CUSTOM ADMIN URLs MUST COME FIRST
    path("admin/coverage/", include("fisability.admin_urls")),

    # Then normal admin
    path('admin/', admin.site.urls),

    # API
    path('api/', include('contactus.urls')),
    path('api/fisability/', include('fisability.urls')),
    path('api/subscription/', include('subscription.urls')),
    path("api/call3cx/", include("call3cx.urls")),
]
