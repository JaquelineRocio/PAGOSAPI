from rest_framework.viewsets import ModelViewSet
from .models import ExpiredPayment
from .serializers import ExpiredPaymentSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny

class ExpiredPaymentViewSet(ModelViewSet):

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