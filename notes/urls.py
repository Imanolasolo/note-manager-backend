from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterUserView, CustomTokenObtainPairView, CustomTokenRefreshView, NoteViewSet

# Create a router and register the NoteViewSet
router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    # JWT Authentication URLs
    path('api/register/', RegisterUserView.as_view(), name='register_user'),  # User Registration
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get JWT tokens
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT tokens

    # Notes CRUD URLs
    path('api/', include(router.urls)),  # Include all the Note-related API endpoints
]
