from rest_framework import viewsets,permissions,filters,mixins
from payment_user.models import PaymentUser
from .serializers import PaymentSerializer
from .pagination import PaymentsPagination

class PaymentsView(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = PaymentsPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__id','=payment_date','=service_v1']
