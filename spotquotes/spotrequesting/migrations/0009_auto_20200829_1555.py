# Generated by Django 3.0.4 on 2020-08-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotrequesting', '0008_offer_offer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_status',
            field=models.CharField(default=False, max_length=8),
        ),
    ]
