from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Notes app URLs (JWT Authentication and CRUD operations)
    path('api/', include('notes.urls')),  # This will include all routes from notes/urls.py

    # Optionally, add any other apps' URLs here
    # path('other_app/', include('other_app.urls')),
]
