# Generated by Django 3.1 on 2020-08-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_auto_20200820_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('serialno', models.IntegerField(db_column='SerialNo', primary_key=True, serialize=False)),
                ('clientname', models.CharField(db_column='ClientName', max_length=100)),
                ('showclientname', models.CharField(blank=True, db_column='ShowClientName', max_length=100, null=True)),
                ('clientnamecht', models.CharField(blank=True, db_column='ClientNameCHT', max_length=100, null=True)),
                ('clientnamejp', models.CharField(blank=True, db_column='ClientNameJP', max_length=100, null=True)),
                ('clientnameen', models.CharField(blank=True, db_column='ClientNameEN', max_length=100, null=True)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
            ],
            options={
                'db_table': 'client_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientProduct',
            fields=[
                ('serialno', models.IntegerField(db_column='SerialNo', primary_key=True, serialize=False)),
                ('clientname', models.CharField(blank=True, db_column='ClientName', max_length=100, null=True)),
                ('productname', models.CharField(blank=True, db_column='ProductName', max_length=100, null=True)),
                ('showproductname', models.CharField(blank=True, db_column='ShowProductName', max_length=100, null=True)),
                ('unitprice', models.IntegerField(blank=True, db_column='UnitPrice', null=True)),
                ('industrytype', models.CharField(blank=True, db_column='IndustryType', max_length=100, null=True)),
                ('producttype', models.CharField(blank=True, db_column='ProductType', max_length=100, null=True)),
                ('hashtag', models.CharField(blank=True, db_column='HashTag', max_length=1000, null=True)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
            ],
            options={
                'db_table': 'client_product',
                'managed': False,
            },
        ),
    ]
