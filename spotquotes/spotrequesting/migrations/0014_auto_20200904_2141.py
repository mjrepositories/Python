# Generated by Django 3.0.4 on 2020-09-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotrequesting', '0013_auto_20200903_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stakeholder',
            name='group',
            field=models.CharField(choices=[('F&D', 'F&D'), ('key_user', 'key_user'), ('carrier', 'carrier'), ('admin', 'admin')], default='key_user', max_length=15),
        ),
    ]
