from accounting.models import *
from rest_framework import viewsets, permissions, authentication
from .serializer import *

class TransactionViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    authentication_classes = [
        authentication.TokenAuthentication
    ]

    serializer_class = TransactionSerializer
    
    def get_queryset(self):
        queryset = Transaction.objects.all()
        return queryset