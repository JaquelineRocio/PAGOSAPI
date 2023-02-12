from rest_framework import serializers
from payment_user.models import PaymentUser, User

class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset = User.objects.all(),slug_field='email')
    
    class Meta:
        model = PaymentUser
        fields = ['id','user','service_v1','amount','payment_date']
        read_only_fields = ['payment_date']
    
    def validate_servicio_v1(self,value):
        if value:
            if value.lower() not in ['netflix','amazon video','hbo','paramount+']:
                raise serializers.ValidationError('Elija una opción válida')
        return value
