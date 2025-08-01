from django.contrib import admin
from django.urls import path, include  # ✅ include must be here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # ✅ this must be present and exactly like this
]
