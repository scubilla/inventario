from django.db import models
from datetime import datetime

# Create your models here.
class Computer(models.Model):
    computer_name = models.CharField(max_length=30)
    IP_address = models.CharField(max_length=30)
    MAC_address = models.CharField(max_length=30)
    users_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    purchase_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    def __str__(self):
        return self.IP_address + ' ' + self.computer_name


