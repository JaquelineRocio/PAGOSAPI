from django.db import models

# Create your models here.
class Service(models.Model):
    """Model definition for Service."""
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.URLField()

    def __str__(self):
        """Unicode representation of Service."""
        return self.name
