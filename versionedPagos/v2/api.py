from pagos.models import Pagos
from .serializers import PagoSerializer
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 
from expired_payments.models import ExpiredPayment
from .serializers import ExpiredPaymentSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny
from services.models import Service
from services.serializers import ServiceSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.get_queryset().order_by('id')
    serializer_class = PagoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]

    search_fields = ['usuario__id', 'fecha_pago', 'servicio']
    throttle_scope = 'pagos'

class ServiceViewSet(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    #http_method_names = ['get', 'post', 'head']
    # permission_classes=[IsAuthenticated]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['destroy','partial_update','update','create']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes=[AllowAny]
        
        return [permission() for permission in permission_classes]
class ExpiredPaymentViewSet(viewsets.ModelViewSet):

    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredPaymentSerializer
    #http_method_names = ['get', 'post', 'head']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['destroy','partial_update','update']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes=[AllowAny]
        return [permission() for permission in permission_classes]