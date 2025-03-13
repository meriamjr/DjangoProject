from django.db import models
from django.contrib.auth.models import User # Importer le modèle User
from products.models import Products
from django.utils.timezone import now

class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
    blank=True)

    status = models.BooleanField(default=False) # Ex. False = non payé, True= payé
    created_at = models.DateTimeField(default=now)
    
    def __str__(self):
        user_display = self.user.username if self.user else "Guest"
        return f"Cart({self.status}, {user_display}, {self.quantity} x {self.product.title})"