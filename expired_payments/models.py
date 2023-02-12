from django.db import models
from payment_user.models import PaymentUser

# Create your models here.
class ExpiredPayment(models.Model):
    payment_user = models.ForeignKey(PaymentUser, on_delete=models.CASCADE)
    penalty_free_amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.payment_user.payment_date
