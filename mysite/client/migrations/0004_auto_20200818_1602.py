# Generated by Django 3.1 on 2020-08-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20200818_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_product',
            name='hashTag',
            field=models.CharField(max_length=200),
        ),
    ]
