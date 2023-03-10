from django.db import models
from users.models import User
from services.models import Service

# Create your models here.

class PaymentUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    service = models.ForeignKey(Service,on_delete=models.CASCADE,related_name='service',null=True)
    service_v1 = models.CharField(max_length=100,null=True)
    amount = models.FloatField(default=0.0)
    payment_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=True)

    def __str__(self):
        return self.user.email
