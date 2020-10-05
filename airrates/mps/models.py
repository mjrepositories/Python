from django.db import models

# Create your models here.

from django.db import models
from django.core.validators import RegexValidator,MinValueValidator


class Airlane(models.Model):
    METRICS = (
        ('KG','KG'),
        ('SHIPMENT','SHIPMENT')
    )
    carrier = models.CharField(max_length=10,null=True)
    laneid = models.CharField(max_length=11,null=True)
    service_lvl = models.CharField(max_length=2,default=0)
    origin_country = models.CharField(
        validators=[RegexValidator(regex='[A-Z]{2}', message='Country code is two letters')], max_length=2, null=True)
    origin_port = models.CharField(
        validators=[RegexValidator(regex='[A-Z]{3}', message='Port code is three letters')], max_length=3, null=True)
    dest_country = models.CharField(
        validators=[RegexValidator(regex='[A-Z]{2}', message='Country code is two letters')], max_length=2, null=True)
    dest_port = models.CharField(
        validators=[RegexValidator(regex='[A-Z]{3}', message='Port code is three letters')], max_length=3, null=True)
    currency = models.CharField(
        validators=[RegexValidator(regex='[A-Z]{3}', message='Currency is three letters')], max_length=3, null=False)
    pickup = models.FloatField(default=0)
    origin_cust = models.FloatField(default=0)
    origin_hand = models.FloatField(default=0)
    airfreight = models.FloatField(default=0)
    dest_cust = models.FloatField(default=0)
    dest_hand = models.FloatField(default=0)
    delivery = models.FloatField(default=0)
    screening = models.FloatField(default=0)
    screening_metric = models.CharField(max_length=8,default='KG', choices=METRICS)
    dgfee = models.FloatField(default=0)
    dg_metric = models.CharField(max_length=8,default='KG', choices=METRICS)

    def __str__(self):
        return self.carrier + ' ' + str(self.laneid)[-9:]
