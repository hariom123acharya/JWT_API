# accounts/views.py
from rest_framework import generics, permissions
from .serializers import RegisterSerializer, UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user




# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsHR, IsAdmin

class HRDashboardView(APIView):
    permission_classes = [IsHR]

    def get(self, request):
        return Response({"message": "Welcome HR, this is your dashboard!"})


class AdminDashboardView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        return Response({"message": "Welcome Admin!"})
