from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from .models import Account
from .serializers import UserSerializer , RegisterSerializer, LoginSerializer ,UserProfileSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

# Register user

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        if not email or not username or not password:
            return Response({"error": "Email, username, and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = Account.objects.create_user(email=email, username=username, password=password, first_name=first_name, last_name=last_name)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


# Login user
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

# Get user details 
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(UserSerializer(user).data)


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user