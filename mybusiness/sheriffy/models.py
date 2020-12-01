from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.user} Profile'




class Item(models.Model):
    Zones = (
        ('Dolnoskaskie', 'Dolnoskaskie'),
        ('Kujawsko-Pomorskie', 'Kujawsko-Pomorskie'),
        ('Lubelskie', 'Lubelskie'),
        ('Lubuskie', 'Lubuskie'),
        ('Lodzkie', 'Lodzkie'),
        ('Malopolskie', 'Malopolskie'),
        ('Mazowieckie', 'Mazowieckie'),
        ('Opolskie', 'Opolskie'),
        ('Podkarpackie', 'Podkarpackie'),
        ('Podlaskie', 'Podlaskie'),
        ('Pomorskie', 'Pomorskie'),
        ('Slaskie', 'Slaskie'),
        ('Swietokrzyskie', 'Swietokrzyskie'),
        ('Warminsko-Mazurskie', 'Warminsko-Mazurskie'),
        ('Wielkopolskie', 'Wielkopolskie'),
        ('Zachodniopomorskie', 'Zachodniopomorskie')

    )



    States = (
        ('Nowe','Nowe'),
        ('Używane','Używane')
    )

    Categories = (
        ('Motoryzacja', 'Motoryzacja'),
        ('Dom', 'Dom'),
        ('Ogrod', 'Ogrod'),
        ('Elektronika', 'Elektronika'),
        ('Moda', 'Moda'),
        ('Rolnictwo', 'Rolnictwo'),
        ('Zwierzeta', 'Zwierzeta'),
        ('Dziecko', 'Dziecko'),
        ('Sport', 'Sport'),
        ('Hobby', 'Hobby'),
        ('Muzyka', 'Muzyka'),
        ('Edukacja', 'Edukacja'),
        ('Materialy Budowlane', 'Materialy Budowlane'),
        ('Zdrowie', 'Zdrowie'),
        ('Uroda', 'Uroda')
    )

    Statuses = (
        ('Aktywne','Aktywne'),
        ('Zamknięte','Zamknięte')
    )


    owner = models.ForeignKey(Profile,null = True,on_delete=models.CASCADE)
    thing = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=1000,null=True)
    zone = models.CharField(max_length=20,null=True,choices=Zones)
    category = models.CharField(max_length=25,null=True,choices=Categories)
    state = models.CharField(max_length=10,null=True,choices=States)
    time_registered = models.DateField(default=timezone.now)
    status = models.CharField(max_length=13,null=True,choices=Statuses)
''' owner = item_1,thing = 'butelka', description = 'Mam super buetelkę do oddania. Pojemność to 1 litr',
zone = 'Slaskie',category= 'Dom',state = 'Nowe',Status = 'Aktywne'
'''
class Image(models.Model):
    item = models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True,upload_to='item_photos')