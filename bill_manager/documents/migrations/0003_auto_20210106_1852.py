# Generated by Django 3.1.4 on 2021-01-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20210106_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energy_bill',
            name='notes',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='gas_bill',
            name='notes',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='home_bill',
            name='notes',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='internet_bill',
            name='notes',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='tv_bill',
            name='notes',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
