from account.models import *
from .serializer import *
from rest_framework import viewsets, authentication, permissions, generics, status
from rest_framework.response import Response

class ChangePasswordViewSet(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreateViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UserInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        authentication.TokenAuthentication
    ]
    serializer_class = UserInfoSerializer

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user)
        return queryset

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        authentication.TokenAuthentication
    ]
    serializer_class = AddressSerializer