from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator,MinValueValidator
from django.contrib.auth.models import User
# Create your models here.

class Stakeholder(models.Model):
    group_type = (
        ('F&D', 'F&D'),
        ('key_user', 'key_user'),
        ('carrier','carrier'),
        ('admin','admin')
    )
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    group = models.CharField(max_length=15, default='key_user', choices=group_type)
    mail = models.CharField(max_length=40)


    def __str__(self):
        return self.mail

"gross_weight = , volume = , origin_country = , origin_port = , dest_country = , dest_port = , spot_status = Open,ship_week = 33,requestor = user"

"gross_weight = 125, volume = 3.4, origin_country = 'NL', origin_port = 'AMS', dest_country = 'BR', dest_port = 'VCP', spot_status = 'Open',ship_week = 33,requestor = user"

class Spot(models.Model):
    STATUSES = (
        ('Open','Open'),
        ('Closed','Closed')
    )
    gross_weight = models.FloatField(null=False,default=0,validators=[MinValueValidator(0)])
    volume = models.FloatField(null=False,default=0,validators=[MinValueValidator(0)])
    origin_country = models.CharField(
        validators=[RegexValidator(regex='[A-Z]{2}', message='Country code is two letters')], max_length=2,null=True)
    origin_port = models.CharField(
        validators=[RegexValidator(regex='[A-Z]{3}', message='Port code is three letters')], max_length=3,null=True)
    dest_country = models.CharField(
        validators=[RegexValidator(regex='[A-Z]{2}', message='Country code is two letters')], max_length=2,null=True)
    dest_port = models.CharField(
        validators=[RegexValidator(regex='[A-Z]{3}', message='Port code is three letters')], max_length=3,null=True)
    time_registered = models.DateField(default=timezone.now)
    spot_status = models.CharField(max_length=6,default='Open', choices=STATUSES)
    ship_week = models.CharField(max_length=2,null=True)
    requestor = models.ForeignKey(Stakeholder,null = True,on_delete=models.CASCADE)

    def __str__(self):
        return self.origin_country + self.origin_port + '-' + self.dest_country +self.dest_port + '-' + self.ship_week

    def get_absolute_url(self):
        return reverse('spot-home')


class Offer(models.Model):
    STATUSES = (
        ('Rejected','Rejected'),
        ('Accepted','Accepted')
    )
    currency = models.CharField(
        validators=[RegexValidator(regex='[A-Z]{3}', message='Currency is three letters')], max_length=3,null=False)
    pickup = models.FloatField(default=0)
    origin_cust = models.FloatField(default=0)
    origin_hand = models.FloatField(default=0)
    airfreight = models.FloatField(default=0)
    dest_cust = models.FloatField(default=0)
    dest_hand = models.FloatField(default=0)
    delivery = models.FloatField(default=0)
    screening = models.FloatField(default=0)
    dgfee = models.FloatField(default=0)
    offer_status = models.CharField(max_length=8,default='Pending', choices=STATUSES)
    closed = models.CharField(max_length=6,default='Open')
    carrier = models.ForeignKey(Stakeholder,null = True,on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot,null = True,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('spot-home')

"currency='USD',pickup=1,origin_cust=30,origin_hand=2,airfreight=1.54,dest_cust=40,dest_hand=3.5,delivery=1.55,screening = 2,dgfee=1,carrier_id=serviceprovider,spot_id=spot"
class Winner(models.Model):
    spot_id = models.ForeignKey(Spot,null = True,on_delete=models.CASCADE)
    carrier_id = models.ForeignKey(Stakeholder,null = True,on_delete=models.CASCADE)


