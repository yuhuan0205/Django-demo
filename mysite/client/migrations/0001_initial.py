# Generated by Django 3.1 on 2020-08-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client_info',
            fields=[
                ('SerialNo', models.AutoField(primary_key=True, serialize=False)),
                ('ClientName', models.CharField(max_length=50)),
                ('ShowClientName', models.CharField(max_length=50)),
                ('ClientNameCHT', models.CharField(max_length=50)),
                ('ClientNameJP', models.CharField(max_length=50)),
                ('ClientNameEN', models.CharField(max_length=50)),
                ('Status', models.BooleanField()),
            ],
        ),
    ]
