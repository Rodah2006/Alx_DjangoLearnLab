from django.contrib import admin
from django.urls import path, include  # include is needed to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include the URLs from your relationship_app
    path('', include('relationship_app.urls')),  # So URLs like /admin_page/ work

    # Optional: you could also do this if you want to prefix your app with 'app/' or similar:
    # path('app/', include('relationship_app.urls')),
]
