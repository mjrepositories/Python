# Generated by Django 3.0.4 on 2020-08-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotrequesting', '0011_auto_20200829_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='closed',
            field=models.CharField(default='Open', max_length=6),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Accepted', 'Accepted')], default='Rejected', max_length=8),
        ),
    ]
