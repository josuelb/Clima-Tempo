from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ClienteSerializer
from .models import Cliente
# Create your views here.


class ClientesViews(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

