from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Your app's main routes
    path('', include('relationship_app.urls')),  # for things like index, book list, etc.

    # Authentication routes: login, register, logout
    path('auth/', include('relationship_app.urls')),  # register, login, logout
]
