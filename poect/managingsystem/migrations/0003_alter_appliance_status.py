# Generated by Django 4.2.16 on 2024-11-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managingsystem', '0002_remove_appliance_appliance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliance',
            name='status',
            field=models.CharField(choices=[('ввімкнений', 'Ввімкнений'), ('вимкнений', 'Вимкнений')], max_length=10),
        ),
    ]