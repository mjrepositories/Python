from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.




# i am creating a model for the offer that will be present on the website placed by users
class Offer(models.Model):
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

     # I am declaring the item for offer
    item = models.CharField(max_length=100)
    # I am declaring the title of the offer
    title = models.CharField(max_length=100)
    # I am declaring the content of the offer here. Text field is unrestricted
    content = models.TextField()
    # I am declaring the time of posting the offer. timezone.now will add current time
    posting_date = models.DateTimeField(default=timezone.now)
    # I am declaring the city
    city = models.CharField(max_length=100)
    # I am declaring the wojewodztwo
    zone = models.CharField(max_length=30,choices=Zones)
    # I am declaring categories
    category = models.CharField(max_length=30,choices=Categories)
    # I am assigning the use to the offer
    # on_delete option with models.CASCADE will cause that the offer to vanish when the user is not present
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    # below command will show the item field when the product is referred
    def __str__(self):
        return self.item



