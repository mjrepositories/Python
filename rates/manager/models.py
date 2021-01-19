from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.



class Employee(models.Model):
    GROUPS = (
        ('Rates Manager','Rates Manager'),
        ('Analyst','Analyst')
    )
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    group = models.CharField(null=True,max_length=13,choices=GROUPS)
    name =  models.CharField(null=True,max_length=15)
    surname = models.CharField(null=True, max_length=30)

    def __str__(self):
        return self.user.username

class Shipmentfcl(models.Model):

    STATUS = (
        ('PENDING',"PENDING"),
        ("SOLVED","SOLVED")
    )

    ACTIONS = (
        ("YES", 'YES'),
        ('NO', 'NO')
    )

    infodis = models.IntegerField(default=0)
    shipment = models.CharField(max_length=15)
    booker_id = models.CharField(max_length=6,null=True,blank=True)
    shipment_booker_name = models.CharField(max_length=40,null=True,blank=True)
    shipper_id = models.CharField(max_length=40,null=True,blank=True)
    consignee_id = models.CharField(max_length=40,null=True,blank=True)
    pickup_city = models.CharField(max_length=40,null=True,blank=True)
    pickup_country = models.CharField(max_length=20,null=True,blank=True)
    port_of_loading = models.CharField(max_length=20,null=True,blank=True)
    port_of_discharge = models.CharField(max_length=20,null=True,blank=True)
    delivery_city = models.CharField(max_length=40,null=True,blank=True)
    delivery_country = models.CharField(max_length=20,null=True,blank=True)
    del_terms = models.CharField(max_length=10,null=True,blank=True)
    container_number = models.CharField(max_length=20,null=True,blank=True)
    bill_of_lading = models.CharField(max_length=20,null=True,blank=True)
    pickup_zip_code = models.CharField(max_length=20,null=True,blank=True)
    hawb = models.CharField(max_length=20,null=True,blank=True)
    delivery_zip_code = models.CharField(max_length=20,null=True,blank=True)
    booking_date = models.DateField(null=True,blank=True)
    leg_1_pickup_planned = models.DateField(null=True,blank=True)
    leg_1_pickup_actual = models.DateField(null=True,blank=True)
    leg_2_pickup_planned = models.DateField(null=True,blank=True)
    leg_2_pickup_actual = models.DateField(null=True,blank=True)
    leg_3_delivery_actual = models.DateField(null=True,blank=True)
    leg_1_carrier_name = models.CharField(max_length=30,null=True,blank=True)
    leg_2_carrier_name = models.CharField(max_length=30,null=True,blank=True)
    leg_3_carrier_name = models.CharField(max_length=30,null=True,blank=True)
    billable_indicator_leg_1 = models.CharField(max_length=3, null=True,blank=True)
    billable_indicator_leg_2 = models.CharField(max_length=3, null=True,blank=True)
    billable_indicator_leg_3 = models.CharField(max_length=3, null=True,blank=True)
    container_type = models.CharField(max_length=30,null=True,blank=True)
    leg_1_transport_mode = models.CharField(max_length=30,null=True,blank=True)
    leg_2_transport_mode = models.CharField(max_length=30,null=True,blank=True)
    leg_3_transport_mode = models.CharField(max_length=30,null=True,blank=True)
    domain_code = models.CharField(max_length=7,null=True,blank=True)
    total_costs_sales = models.DecimalField(null=True,decimal_places=2,max_digits=10)
    leg_1_total_costs_purchase = models.DecimalField(null=True,decimal_places=2,max_digits=10)
    leg_2_total_costs_purchase = models.DecimalField(null=True,decimal_places=2,max_digits=10)
    leg_3_total_costs_purchase = models.DecimalField(null=True,decimal_places=2,max_digits=10)
    pallets = models.IntegerField(null=True)
    weight = models.DecimalField(null=True,decimal_places=2,max_digits=10)
    volume = models.DecimalField(null=True,decimal_places=2,max_digits=10)
    action_taken = models.CharField(max_length=3,blank=True,null=True,choices=ACTIONS)
    pending_solved = models.CharField(max_length=7,blank=True,null=True,choices=STATUS)
    mail_sent = models.CharField(max_length=3,blank=True,null=True,choices=ACTIONS)
    date_of_email = models.DateField(null=True,blank=True)
    email_subject = models.CharField(max_length=100,blank=True,null=True)
    delay_in_answer = models.IntegerField(null=True,blank=True)
    comments = models.CharField(max_length=350,null=True,blank=True)

    def __str__(self):
        return self.shipment

    @property
    def page(self):
        if self.domain_code == 'CL':
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=DAP"
        elif self.domain_code == "PHILIPSM1":
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=PHILIPSM1"
        else:
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=PHILIPSR1"

class Shipmentlcl(models.Model):

    STATUS = (
        ('PENDING',"PENDING"),
        ("SOLVED","SOLVED")
    )

    ACTIONS = (
        ("YES",'YES'),
        ('NO','NO')
    )

    infodis = models.IntegerField(default=0)
    shipment = models.CharField(max_length=15)
    booker_id = models.CharField(max_length=6, null=True, blank=True)
    shipment_booker_name = models.CharField(max_length=40, null=True, blank=True)
    shipper_id = models.CharField(max_length=40, null=True, blank=True)
    consignee_id = models.CharField(max_length=40, null=True, blank=True)
    pickup_city = models.CharField(max_length=40, null=True, blank=True)
    pickup_country = models.CharField(max_length=20, null=True, blank=True)
    port_of_loading = models.CharField(max_length=20, null=True, blank=True)
    port_of_discharge = models.CharField(max_length=20, null=True, blank=True)
    delivery_city = models.CharField(max_length=40, null=True, blank=True)
    delivery_country = models.CharField(max_length=20, null=True, blank=True)
    del_terms = models.CharField(max_length=10, null=True, blank=True)
    container_number = models.CharField(max_length=20, null=True, blank=True)
    bill_of_lading = models.CharField(max_length=20, null=True, blank=True)
    pickup_zip_code = models.CharField(max_length=20, null=True, blank=True)
    hawb = models.CharField(max_length=20, null=True, blank=True)
    delivery_zip_code = models.CharField(max_length=20, null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    leg_1_pickup_planned = models.DateField(null=True, blank=True)
    leg_1_pickup_actual = models.DateField(null=True, blank=True)
    leg_2_pickup_planned = models.DateField(null=True, blank=True)
    leg_2_pickup_actual = models.DateField(null=True, blank=True)
    leg_3_delivery_actual = models.DateField(null=True, blank=True)
    leg_1_carrier_name = models.CharField(max_length=30, null=True, blank=True)
    leg_2_carrier_name = models.CharField(max_length=30, null=True, blank=True)
    leg_3_carrier_name = models.CharField(max_length=30, null=True, blank=True)
    billable_indicator_leg_1 = models.CharField(max_length=3, null=True, blank=True)
    billable_indicator_leg_2 = models.CharField(max_length=3, null=True, blank=True)
    billable_indicator_leg_3 = models.CharField(max_length=3, null=True, blank=True)
    container_type = models.CharField(max_length=30, null=True, blank=True)
    leg_1_transport_mode = models.CharField(max_length=30, null=True, blank=True)
    leg_2_transport_mode = models.CharField(max_length=30, null=True, blank=True)
    leg_3_transport_mode = models.CharField(max_length=30, null=True, blank=True)
    domain_code = models.CharField(max_length=7, null=True, blank=True)
    total_costs_sales = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    leg_1_total_costs_purchase = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    leg_2_total_costs_purchase = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    leg_3_total_costs_purchase = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    pallets = models.IntegerField(null=True)
    weight = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    volume = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    action_taken = models.CharField(max_length=3, blank=True, null=True, choices=ACTIONS)
    pending_solved = models.CharField(max_length=7, blank=True, null=True, choices=STATUS)
    mail_sent = models.CharField(max_length=3, blank=True, null=True, choices=ACTIONS)
    date_of_email = models.DateField(null=True, blank=True)
    email_subject = models.CharField(max_length=100, blank=True, null=True)
    delay_in_answer = models.IntegerField(null=True, blank=True)
    comments = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return self.shipment

    @property
    def page(self):
        if self.domain_code == 'CL':
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=DAP"
        elif self.domain_code == "PHILIPSM1":
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=PHILIPSM1"
        else:
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=PHILIPSR1"


class Shipmentair(models.Model):

    STATUS = (
        ('PENDING',"PENDING"),
        ("SOLVED","SOLVED")
    )

    ACTIONS = (
        ("YES", 'YES'),
        ('NO', 'NO')
    )

    infodis = models.IntegerField(default=0)
    shipment = models.CharField(max_length=15)
    booker_id = models.CharField(max_length=6, null=True, blank=True)
    shipment_booker_name = models.CharField(max_length=40, null=True, blank=True)
    shipper_id = models.CharField(max_length=40, null=True, blank=True)
    consignee_id = models.CharField(max_length=40, null=True, blank=True)
    pickup_city = models.CharField(max_length=40, null=True, blank=True)
    pickup_country = models.CharField(max_length=20, null=True, blank=True)
    port_of_loading = models.CharField(max_length=20, null=True, blank=True)
    port_of_discharge = models.CharField(max_length=20, null=True, blank=True)
    delivery_city = models.CharField(max_length=40, null=True, blank=True)
    delivery_country = models.CharField(max_length=20, null=True, blank=True)
    del_terms = models.CharField(max_length=10, null=True, blank=True)
    container_number = models.CharField(max_length=20, null=True, blank=True)
    bill_of_lading = models.CharField(max_length=20, null=True, blank=True)
    pickup_zip_code = models.CharField(max_length=20, null=True, blank=True)
    hawb = models.CharField(max_length=20, null=True, blank=True)
    delivery_zip_code = models.CharField(max_length=20, null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    leg_1_pickup_planned = models.DateField(null=True, blank=True)
    leg_1_pickup_actual = models.DateField(null=True, blank=True)
    leg_2_pickup_planned = models.DateField(null=True, blank=True)
    leg_2_pickup_actual = models.DateField(null=True, blank=True)
    leg_3_delivery_actual = models.DateField(null=True, blank=True)
    leg_1_carrier_name = models.CharField(max_length=30, null=True, blank=True)
    leg_2_carrier_name = models.CharField(max_length=30, null=True, blank=True)
    leg_3_carrier_name = models.CharField(max_length=30, null=True, blank=True)
    billable_indicator_leg_1 = models.CharField(max_length=3, null=True, blank=True)
    billable_indicator_leg_2 = models.CharField(max_length=3, null=True, blank=True)
    billable_indicator_leg_3 = models.CharField(max_length=3, null=True, blank=True)
    container_type = models.CharField(max_length=30, null=True, blank=True)
    leg_1_transport_mode = models.CharField(max_length=30, null=True, blank=True)
    leg_2_transport_mode = models.CharField(max_length=30, null=True, blank=True)
    leg_3_transport_mode = models.CharField(max_length=30, null=True, blank=True)
    domain_code = models.CharField(max_length=7, null=True, blank=True)
    total_costs_sales = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    leg_1_total_costs_purchase = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    leg_2_total_costs_purchase = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    leg_3_total_costs_purchase = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    pallets = models.IntegerField(null=True)
    weight = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    volume = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    action_taken = models.CharField(max_length=3, blank=True, null=True, choices=ACTIONS)
    pending_solved = models.CharField(max_length=7, blank=True, null=True, choices=STATUS)
    mail_sent = models.CharField(max_length=3, blank=True, null=True, choices=ACTIONS)
    date_of_email = models.DateField(null=True, blank=True)
    email_subject = models.CharField(max_length=100, blank=True, null=True)
    delay_in_answer = models.IntegerField(null=True, blank=True)
    comments = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return self.shipment

    @property
    def page(self):
        if self.domain_code == 'CL':
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=DAP"
        elif self.domain_code == "PHILIPSM1":
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=PHILIPSM1"
        else:
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=PHILIPSR1"


class Shipmentroadeu(models.Model):

    STATUS = (
        ('PENDING',"PENDING"),
        ("SOLVED","SOLVED")
    )

    ACTIONS = (
        ("YES", 'YES'),
        ('NO', 'NO')
    )

    infodis = models.IntegerField(default=0)
    shipment = models.CharField(max_length=15)
    booker_id = models.CharField(max_length=6, null=True, blank=True)
    shipment_booker_name = models.CharField(max_length=40, null=True, blank=True)
    shipper_id = models.CharField(max_length=40, null=True, blank=True)
    consignee_id = models.CharField(max_length=40, null=True, blank=True)
    pickup_city = models.CharField(max_length=40, null=True, blank=True)
    pickup_country = models.CharField(max_length=20, null=True, blank=True)
    port_of_loading = models.CharField(max_length=20, null=True, blank=True)
    port_of_discharge = models.CharField(max_length=20, null=True, blank=True)
    delivery_city = models.CharField(max_length=40, null=True, blank=True)
    delivery_country = models.CharField(max_length=20, null=True, blank=True)
    del_terms = models.CharField(max_length=10, null=True, blank=True)
    container_number = models.CharField(max_length=20, null=True, blank=True)
    bill_of_lading = models.CharField(max_length=20, null=True, blank=True)
    pickup_zip_code = models.CharField(max_length=20, null=True, blank=True)
    hawb = models.CharField(max_length=20, null=True, blank=True)
    delivery_zip_code = models.CharField(max_length=20, null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    leg_1_pickup_planned = models.DateField(null=True, blank=True)
    leg_1_pickup_actual = models.DateField(null=True, blank=True)
    leg_2_pickup_planned = models.DateField(null=True, blank=True)
    leg_2_pickup_actual = models.DateField(null=True, blank=True)
    leg_3_delivery_actual = models.DateField(null=True, blank=True)
    leg_1_carrier_name = models.CharField(max_length=30, null=True, blank=True)
    leg_2_carrier_name = models.CharField(max_length=30, null=True, blank=True)
    leg_3_carrier_name = models.CharField(max_length=30, null=True, blank=True)
    billable_indicator_leg_1 = models.CharField(max_length=3, null=True, blank=True)
    billable_indicator_leg_2 = models.CharField(max_length=3, null=True, blank=True)
    billable_indicator_leg_3 = models.CharField(max_length=3, null=True, blank=True)
    container_type = models.CharField(max_length=30, null=True, blank=True)
    leg_1_transport_mode = models.CharField(max_length=30, null=True, blank=True)
    leg_2_transport_mode = models.CharField(max_length=30, null=True, blank=True)
    leg_3_transport_mode = models.CharField(max_length=30, null=True, blank=True)
    domain_code = models.CharField(max_length=7, null=True, blank=True)
    total_costs_sales = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    leg_1_total_costs_purchase = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    leg_2_total_costs_purchase = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    leg_3_total_costs_purchase = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    pallets = models.IntegerField(null=True)
    weight = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    volume = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    action_taken = models.CharField(max_length=3, blank=True, null=True, choices=ACTIONS)
    pending_solved = models.CharField(max_length=7, blank=True, null=True, choices=STATUS)
    mail_sent = models.CharField(max_length=3, blank=True, null=True, choices=ACTIONS)
    date_of_email = models.DateField(null=True, blank=True)
    email_subject = models.CharField(max_length=100, blank=True, null=True)
    delay_in_answer = models.IntegerField(null=True, blank=True)
    comments = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return self.shipment

    @property
    def page(self):
        if self.domain_code == 'CL':
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=DAP"
        elif self.domain_code == "PHILIPSM1":
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=PHILIPSM1"
        else:
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=PHILIPSR1"


class Shipmentroadus(models.Model):

    STATUS = (
        ('PENDING',"PENDING"),
        ("SOLVED","SOLVED")
    )

    ACTIONS = (
        ("YES", 'YES'),
        ('NO', 'NO')
    )

    infodis = models.IntegerField(default=0)
    shipment = models.CharField(max_length=15)
    booker_id = models.CharField(max_length=6, null=True, blank=True)
    shipment_booker_name = models.CharField(max_length=40, null=True, blank=True)
    shipper_id = models.CharField(max_length=40, null=True, blank=True)
    consignee_id = models.CharField(max_length=40, null=True, blank=True)
    pickup_city = models.CharField(max_length=40, null=True, blank=True)
    pickup_country = models.CharField(max_length=20, null=True, blank=True)
    port_of_loading = models.CharField(max_length=20, null=True, blank=True)
    port_of_discharge = models.CharField(max_length=20, null=True, blank=True)
    delivery_city = models.CharField(max_length=40, null=True, blank=True)
    delivery_country = models.CharField(max_length=20, null=True, blank=True)
    del_terms = models.CharField(max_length=10, null=True, blank=True)
    container_number = models.CharField(max_length=20, null=True, blank=True)
    bill_of_lading = models.CharField(max_length=20, null=True, blank=True)
    pickup_zip_code = models.CharField(max_length=20, null=True, blank=True)
    hawb = models.CharField(max_length=20, null=True, blank=True)
    delivery_zip_code = models.CharField(max_length=20, null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    leg_1_pickup_planned = models.DateField(null=True, blank=True)
    leg_1_pickup_actual = models.DateField(null=True, blank=True)
    leg_2_pickup_planned = models.DateField(null=True, blank=True)
    leg_2_pickup_actual = models.DateField(null=True, blank=True)
    leg_3_delivery_actual = models.DateField(null=True, blank=True)
    leg_1_carrier_name = models.CharField(max_length=30, null=True, blank=True)
    leg_2_carrier_name = models.CharField(max_length=30, null=True, blank=True)
    leg_3_carrier_name = models.CharField(max_length=30, null=True, blank=True)
    billable_indicator_leg_1 = models.CharField(max_length=3, null=True, blank=True)
    billable_indicator_leg_2 = models.CharField(max_length=3, null=True, blank=True)
    billable_indicator_leg_3 = models.CharField(max_length=3, null=True, blank=True)
    container_type = models.CharField(max_length=30, null=True, blank=True)
    leg_1_transport_mode = models.CharField(max_length=30, null=True, blank=True)
    leg_2_transport_mode = models.CharField(max_length=30, null=True, blank=True)
    leg_3_transport_mode = models.CharField(max_length=30, null=True, blank=True)
    domain_code = models.CharField(max_length=7, null=True, blank=True)
    total_costs_sales = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    leg_1_total_costs_purchase = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    leg_2_total_costs_purchase = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    leg_3_total_costs_purchase = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    pallets = models.IntegerField(null=True)
    weight = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    volume = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    action_taken = models.CharField(max_length=3, blank=True, null=True, choices=ACTIONS)
    pending_solved = models.CharField(max_length=7, blank=True, null=True, choices=STATUS)
    mail_sent = models.CharField(max_length=3, blank=True, null=True, choices=ACTIONS)
    date_of_email = models.DateField(null=True, blank=True)
    email_subject = models.CharField(max_length=100, blank=True, null=True)
    delay_in_answer = models.IntegerField(null=True, blank=True)
    comments = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return self.shipment

    @property
    def page(self):
        if self.domain_code =='CL':
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=DAP"
        elif self.domain_code =="PHILIPSM1":
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=PHILIPSM1"
        else:
            return f"https://www.infodis.net/philips/net/Shipment/Details?InfodisNumber={self.infodis}&DomainCode=PHILIPSR1"




class ShipmentsOverview(models.Model):
    number_all = models.IntegerField(null=True)
    missing_src = models.IntegerField(null=True)
    missing_matc = models.IntegerField(null=True)
    missing_dap = models.IntegerField(null=True)
    date_registered = models.DateField(default=datetime.date.today)


class ShipmentOverviewHistory(models.Model):
    coverage_all = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    reporting_date = models.DateField()

class ImportingFile(models.Model):
    file = models.FileField()