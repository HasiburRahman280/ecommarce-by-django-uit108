from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShipingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name  = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)
    full_address  = models.TextField()
    order_note  = models.TextField()


    def __str__(self):
        return self.user.username
