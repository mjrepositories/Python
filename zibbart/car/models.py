from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.





class Repair(models.Model):
    BRANDS = (
        ('AUDI', 'AUDI'), ('BMW', 'BMW'), ('CHEVROLET', 'CHEVROLET'), ('CITROEN', 'CITROEN'), ('FIAT', 'FIAT'),
        ('FORD', 'FORD'), ('HONDA', 'HONDA'), ('HYUNDAI', 'HYUNDAI'), ('KIA', 'KIA'), ('MAZDA', 'MAZDA'),
        ('MERCEDES', 'MERCEDES'), ('MITSUBISHI', 'MITSUBISHI'), ('NISSA', 'NISSAN'), ('OPEL', 'OPEL'),
        ('PEUGEOT', 'PEUGEOT'), ('RENAULT', 'RENAULT'), ('SEAT', 'SEAT'), ('SKODA', 'SKODA'),
        ('TOYOTA', 'TOYOTA'), ('VOLKSWAGEN', 'VOLKSWAGEN')
    )
    car = models.CharField(max_length=15, null=True, choices=BRANDS)
    fix_date = models.DateTimeField(default=timezone.now)
    plate = models.CharField(max_length=10, null=True)


    def __str__(self):
        return self.car + " - " + self.plate


class Service(models.Model):

    SERVICE  = (
        ('USŁUGA','USŁUGA'), ('CZĘŚĆ','CZĘŚĆ')
    )
    service_provided = models.CharField(max_length=50,null=True)
    product_provided = models.CharField(max_length=50,null=True)
    what_provided = models.CharField(max_length=8,null=True,choices=SERVICE)
    price = models.FloatField(null=False, default=0, validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)], default=1)
    repair = models.ForeignKey(Repair,null = True,on_delete=models.CASCADE)


    def __str__(self):
        return self.repair.plate + " - " + self.what_provided + " - " + self.service_provided + self.product_provided
