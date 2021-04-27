from django.db import models

# Create your models here.

class Person(models.Model):

    #  Employees = (
        # ('Maciej Janowski', 'Maciej Janowski'),
        # ('Bartosz Pryca', 'Bartosz Pryca'),
        # ('Agnieszka Reguła', 'Agnieszka Reguła'),
        # ('Patryk Tomaszewski', 'Patryk Tomaszewski'),
        # ('Adam Ogłaza', 'Adam Ogłaza'),
        # ('Magdalena Kotynia', 'Magdalena Kotynia'),
        # ('Roman Kowalski', 'Roman Kowalski'),
   
    # )

    firstname = models.CharField(max_length=20,null=True)
    lastname = models.CharField(max_length=30,null=True)

    @property
    def employee(self):
        return self.firstname + " " + self.lastname

    def __str__(self):
        return self.employee


class Instruction(models.Model):
    progress = (
        ('In progress','In progress'),
        ('Updated','Updated')
    )

    name = models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=20,null=True,blank=True,choices=progress)
    link = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.name

class Business(models.Model):
    # area = (
    #     ('AWM','AWM'),
    #     ('BB','BB'),
    #     ('GF','GF'),
    #     ('LC&I','LC&I'),
    #     ('Nordea','Nordea'),
    #     ('PEB','PEB')
    # )
    business_area = models.CharField(max_length=6,null=True)

    def __str__(self):
        return self.business_area


class Report(models.Model):
    deadline_period = (
        ('BD 1','BD 1'),
        ('BD 2','BD 2'),
        ('BD 3','BD 3'),
        ('BD 4','BD 4'),
        ('BD 5','BD 5'),
        ('BD 6','BD 6'),
        ('BD 7','BD 7'),
        ('BD 8','BD 8'),
        ('BD 9','BD 9'),
        ('BD 10','BD 10'),
        ('BD 11','BD 11'),
        ('BD 12','BD 12'),
        ('BD 13','BD 13'),
        ('BD 14','BD 14'),
        ('BD 15','BD 15') 
    )
    
    title = models.CharField(max_length=200,null=True)
    owner = models.ForeignKey(Person,null = True,on_delete=models.SET_NULL,related_name='owner')
    back_up = models.ForeignKey(Person,null = True,on_delete=models.SET_NULL,related_name='backup')
    business_area = models.ForeignKey(Business,null=True,on_delete=models.SET_NULL)
    deadline = models.CharField(max_length=5,null=True,choices=deadline_period)
    instruction = models.ForeignKey(Instruction,null=True,blank=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title



class Period(models.Model):
    Banking_day = (
        ('BD 1','BD 1'),
        ('BD 2','BD 2'),
        ('BD 3','BD 3'),
        ('BD 4','BD 4'),
        ('BD 5','BD 5'),
        ('BD 6','BD 6'),
        ('BD 7','BD 7'),
        ('BD 8','BD 8'),
        ('BD 9','BD 9'),
        ('BD 10','BD 10'),
        ('BD 11','BD 11'),
        ('BD 12','BD 12'),
        ('BD 13','BD 13'),
        ('BD 14','BD 14'),
        ('BD 15','BD 15') 
    )

    Quarter = (
        ('Q1','Q1'),
        ('Q2','Q2'),
        ('Q3','Q3'),
        ('Q4','Q4'),
    )

    Month = (
        ('January','January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December')
    )

    Years = (
        (2021,2021),
        (2022,2022),
        (2023,2023),
        (2024,2024),
        (2025,2025),
        (2026,2026),
    )
    reporting_period = models.CharField(max_length=6,null=True,choices=Banking_day)
    month = models.CharField(max_length=20,null=True,choices=Month)
    quarter = models.CharField(max_length=2,null=True,choices=Quarter)
    year = models.CharField(max_length=4,null=True,choices=Years)




    def __str__(self):
        return f'{self.reporting_period} {self.month} {str(self.year)}'


class ReportingPeriod(models.Model):
    Month = (
        ('January','January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December')
    )

    Years = (
        (2021,2021),
        (2022,2022),
        (2023,2023),
        (2024,2024),
        (2025,2025),
        (2026,2026),
    )

    month = models.CharField(max_length=15,null=True,choices=Month)
    year = models.CharField(max_length=4,null=True,choices=Years)

    def __str__(self):
        return f'{self.month} {self.year}'

class Status(models.Model):
    yes_no = (
        ('YES','YES'),
        ('NO','NO')
    )

    report = models.ForeignKey(Report,null=True,on_delete=models.SET_NULL)
    reporting_period = models.ForeignKey(ReportingPeriod,null=True,on_delete=models.SET_NULL)
    executed = models.CharField(max_length=3,null=True,blank=True,choices=yes_no)
    executed_on = models.ForeignKey(Period,null=True,blank=True,on_delete=models.SET_NULL)
    on_time = models.CharField(max_length=3,null=True,blank=True,choices=yes_no)
    issues = models.CharField(max_length=3,null=True,blank=True,choices=yes_no)
    issues_description = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return f'{self.report} / owner - {self.report.owner} / period - {self.reporting_period}'


