# Generated by Django 3.1.4 on 2021-01-09 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20210109_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmentair',
            name='comments',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='shipmentfcl',
            name='comments',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='shipmentlcl',
            name='comments',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='shipmentroadeu',
            name='comments',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='shipmentroadus',
            name='comments',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]