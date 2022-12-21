from rest_framework.serializers import ModelSerializer
from .models import ExpiredPayment


class ExpiredPaymentSerializer(ModelSerializer):

    class Meta:
        model = ExpiredPayment
        fields = '__all__'