# Generated by Django 3.1.4 on 2021-01-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20210106_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energy_bill',
            name='consumption',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='energy_bill',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='gas_bill',
            name='consumption',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='gas_bill',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='home_bill',
            name='consumption_cold',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='home_bill',
            name='consumption_warm',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='home_bill',
            name='price_cold',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='home_bill',
            name='price_warm',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='internet_bill',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='tv_bill',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
