from rest_framework import status, permissions, generics, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# User Registration View (JWT Authentication)
class RegisterUserView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Extract the username from the serializer data
        username = serializer.validated_data.get('username')

        # Check if the username already exists
        if get_user_model().objects.filter(username=username).exists():
            return Response(
                {"error": "Username already taken"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Hash the password before saving the user
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])

        # If the username is unique, save the user
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        # Return the JWT tokens
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)


# JWT Token View for obtaining and refreshing JWT
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]


# Note CRUD Views
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Save the note with the user making the request
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Filter the notes by the logged-in user
        return Note.objects.filter(user=self.request.user)