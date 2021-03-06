# Generated by Django 3.0.4 on 2020-08-16 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotrequesting', '0005_auto_20200816_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='carrier',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='spotrequesting.Stakeholder'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='spot',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='spotrequesting.Spot'),
        ),
    ]
