# Generated by Django 3.1 on 2020-08-18 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20200818_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client_product',
            name='clientName',
        ),
        migrations.DeleteModel(
            name='Client_info',
        ),
        migrations.DeleteModel(
            name='Client_product',
        ),
    ]
