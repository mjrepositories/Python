from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

# I am creating a model for ticket raised
class Ticket(models.Model):
    STATUSES = (
        ('New', 'New'),
        ('Pending', 'Pending'),
        ('Solved','Solved')
    )

    ISSUES = (
        ('Password expired', "Password expired"),
        ('Account blocked','Account blocked'),
        ("Don't remember the password","Don't remember the password"),
        ("Other","Other")

    )

    KUSER = (
        ('Erik Alexander','Erik Alexander'),
        ('Nadja Quesada','Nadja Quesada'),
        ("Mellen Lopez","Mellen Lopez"),
        ('Krystian Krawczyk','Krystian Krawczyk'),
        ("Maciej Janowski",'Maciej Janowski')
    )
    issue = models.CharField(max_length=30,choices=ISSUES)
    content = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUSES,default='New')
    kuser = models.CharField(max_length=20, choices=KUSER)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.issue

    def get_absolute_url(self):
        return reverse('keyuser-overview')

