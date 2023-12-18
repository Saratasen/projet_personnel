from django.db import models
from django.contrib.auth.models import User

class Facture(models.Model):
    SEX_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=132)
    address = models.CharField(max_length=64)
    sex = models.CharField(max_length=1 ,choices=SEX_TYPES)

    def __str__(self):
        return f"Facture #{self.id} - {self.user.username} - {self.amount}€"
