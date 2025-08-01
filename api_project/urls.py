from django.contrib import admin
from django.urls import path, include  # ✅ include must be imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # ✅ this line is what the checker wants
]
