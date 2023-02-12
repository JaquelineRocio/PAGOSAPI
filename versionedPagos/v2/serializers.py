from services.models import Service
from services.models import Service
from rest_framework import serializers
from expired_payments.models import ExpiredPayment
from users.models import User
from payment_user.models import PaymentUser

class PaymentSerializerV2(serializers.ModelSerializer):
    user=serializers.SlugRelatedField(queryset=User.objects.all(),slug_field="email")
    class Meta:
            model = PaymentUser
            fields = ['id','user','service','amount','payment_date','expiration_date']
            read_only_fields = ['payment_date']


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        model = Service
        fields = '__all__'

class ExpiredPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpiredPayment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        read_only=("password",)
