from rest_framework import serializers
from pagos.models import Pagos
from expired_payments.models import ExpiredPayment

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = '__all__'
        read_only_fields = '__all__',

class ExpiredPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpiredPayment
        fields = '__all__'