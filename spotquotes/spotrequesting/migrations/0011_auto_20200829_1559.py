# Generated by Django 3.0.4 on 2020-08-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotrequesting', '0010_auto_20200829_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_status',
            field=models.CharField(default=None, max_length=8),
        ),
    ]
