from django.db import models
from django.core.validators import DecimalValidator
# Create your models here.

class energy_bill(models.Model):
    PAID = (
        ("YES","YES"),
        ("NO", "NO")
    )

    PERIODS = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    )

    YEARS = (
        (2021, 2021),
        (2022, 2022),
        (2023, 2023),
        (2024, 2024),
        (2025, 2025),
    )

    price = models.DecimalField(null=True,decimal_places=2,max_digits=5)
    paid = models.CharField(null=True,max_length=3,choices=PAID)
    consumption = models.DecimalField(null=True,decimal_places=2,max_digits=5)
    period = models.CharField(null=True,choices=PERIODS,max_length=9)
    year = models.IntegerField(null=True, choices=YEARS)
    date = models.DateField()
    notes = models.CharField(null=True, blank=True, max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to='bill_photos')

    @property
    def summary(self):
        return round(self.price * self.consumption,2)

    def __str__(self):
        return f'Electricity / {str(self.summary)} /{str(self.period)} / {str(self.year)}'




class gas_bill(models.Model):
    PAID = (
        ("YES","YES"),
        ("NO", "NO")
    )

    PERIODS = (
        ('January - February', 'January - February'),
        ('March - April', 'March - April'),
        ('May - June', 'May - June'),
        ('July - August', 'July - August'),
        ('September - October', 'September - October'),
        ('November - December', 'November - December')
    )

    YEARS = (
        (2021, 2021),
        (2022, 2022),
        (2023, 2023),
        (2024, 2024),
        (2025, 2025),
    )
    price = models.DecimalField(null=True,decimal_places=2,max_digits=5)
    paid = models.CharField(null=True,max_length=3,choices=PAID)
    consumption = models.DecimalField(null=True,decimal_places=2,max_digits=5)
    period = models.CharField(null=True, choices=PERIODS,max_length=19)
    year = models.IntegerField(null=True, choices=YEARS)
    date = models.DateField()
    notes = models.CharField(null=True, blank=True, max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to='bill_photos')

    @property
    def summary(self):
        return round(self.price * self.consumption,2)

    def __str__(self):
        return f'Gas / {str(self.summary)} /{str(self.period)} / {str(self.year)}'

class home_bill(models.Model):
    PAID = (
        ("YES","YES"),
        ("NO", "NO")
    )

    PERIODS = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    )

    YEARS = (
        (2021, 2021),
        (2022, 2022),
        (2023, 2023),
        (2024, 2024),
        (2025, 2025),
    )

    price_warm = models.DecimalField(null=True,decimal_places=2,max_digits=5)
    consumption_warm = models.DecimalField(null=True,decimal_places=2,max_digits=5)
    price_cold = models.DecimalField(null=True,decimal_places=2,max_digits=5)
    consumption_cold = models.DecimalField(null=True,decimal_places=2,max_digits=5)
    paid = models.CharField(null=True, max_length=3, choices=PAID)
    period = models.CharField(null=True, choices=PERIODS,max_length=9)
    year = models.IntegerField(null=True, choices=YEARS)
    date = models.DateField()
    notes = models.CharField(null=True, blank=True, max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to='bill_photos')

    @property
    def warm_calculation(self):
        return round(self.price_warm * self.consumption_warm,2)

    @property
    def cold_calculation(self):
        return round(self.price_cold * self.consumption_cold,2)

    def __str__(self):
        return f'Home / cold - {str(self.cold_calculation)} || warm - {str(self.warm_calculation)} ' \
               f'/{str(self.period)} / {str(self.year)}'

class tv_bill(models.Model):
    PAID = (
        ("YES", "YES"),
        ("NO", "NO")
    )

    PERIODS = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    )
    YEARS = (
        (2021, 2021),
        (2022, 2022),
        (2023, 2023),
        (2024, 2024),
        (2025, 2025),
    )

    price = models.DecimalField(null=True,decimal_places=2,max_digits=5)
    paid = models.CharField(null=True,max_length=3,choices=PAID)
    period = models.CharField(null=True, choices=PERIODS,max_length=9)
    year = models.IntegerField(null=True, choices=YEARS)
    date = models.DateField()
    notes = models.CharField(null=True, blank=True, max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to='bill_photos')

    def __str__(self):
        return f'TV / {str(self.price)} /{str(self.period)} / {str(self.year)}'

class internet_bill(models.Model):
    PAID = (
        ("YES","YES"),
        ("NO", "NO")
    )

    PERIODS = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    )

    YEARS = (
        (2021, 2021),
        (2022, 2022),
        (2023, 2023),
        (2024, 2024),
        (2025, 2025),
    )

    price = models.DecimalField(null=True,decimal_places=2,max_digits=5)
    paid = models.CharField(null=True,max_length=3,choices=PAID)
    period = models.CharField(null=True, choices=PERIODS,max_length=9)
    year = models.IntegerField(null=True, choices=YEARS)
    date = models.DateField()
    notes = models.CharField(null=True,blank=True, max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to='bill_photos')

    def __str__(self):
        return f'Internet / {str(self.price)} /{str(self.period)} / {str(self.year)}'