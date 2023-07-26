from django.db import models
from datetime import datetime

# Create your models here.

class Operating_system(models.Model):
    operating_system = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.operating_system


class Computer(models.Model):
    computer_name = models.CharField(max_length=30, blank=True)
    IP_address = models.CharField(max_length=30)
    MAC_address = models.CharField(max_length=30)
    operating_system = models.ManyToManyField(Operating_system,max_length=30, blank=True)
    users_name = models.CharField(max_length=30,blank=True)
    location = models.CharField(max_length=30)
    purchase_date = models.DateField('Fecha compra (dd/mm/2023)', auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    def __unicode__(self):
        return self.IP_address + ' ' + self.computer_name


