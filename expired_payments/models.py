from django.db import models
from pagos.models import Pago

# Create your models here.
class ExpiredPayment(models.Model):
    """Model definition for ExpiredPayment."""
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    penalty_free_amount = models.FloatField(default=0.0)

    def __str__(self):
        """Unicode representation of ExpiredPayment."""
        return self.pago.fecha_pago
