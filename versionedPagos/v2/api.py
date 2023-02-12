from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny
from services.models import Service
from users.models import User
from expired_payments.models import ExpiredPayment
from .serializers import ServiceSerializer,UserSerializer, ExpiredPaymentSerializer,PaymentSerializerV2
from users.serializers import RegisterSerializer
from payment_user.models import PaymentUser
from .pagination import PaymentsPaginationV2
from rest_framework import filters
from .throttle import v2RateThrottle

class PaymentsViewV2(ModelViewSet):
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentSerializerV2
    pagination_class = PaymentsPaginationV2
    filter_backends = [filters.SearchFilter]
    search_fields = ['=payment_date','=expiration_date']
    throttle_classes = [v2RateThrottle]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['partial_update','update','destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]     
        return [permission() for permission in permission_classes]
        
    def create(self, request, *args, **kwargs):
        payment = super().create(request, *args, **kwargs)
        last_payment = PaymentUser.objects.order_by('-id').first()
        payment_db = PaymentUser.objects.get(id=last_payment.id)
        if payment_db.expiration_date < payment_db.payment_date:
            penalty = payment_db.amount*0.15
            expired_payment = ExpiredPayment(payment_user=payment_db,penalty_free_amount=penalty)
            expired_payment.save()
        return payment

class ServiceViewSet(ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['destroy','partial_update','update','create']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes=[IsAuthenticated]
        
        return [permission() for permission in permission_classes]


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
            permission_classes=[IsAuthenticated]
        return [permission() for permission in permission_classes]


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_classes = {
        'create': RegisterSerializer,
        
    }
    default_serializer_class = UserSerializer 

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['destroy','partial_update','update','create','retrieve']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes=[IsAuthenticated]
        
        return [permission() for permission in permission_classes]