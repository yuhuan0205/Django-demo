# Generated by Django 3.1 on 2020-08-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_v_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrosWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, db_column='Date', null=True)),
                ('ga1', models.TextField(blank=True, db_column='GA1', null=True)),
                ('ga2', models.TextField(blank=True, db_column='GA2', null=True)),
                ('ga3', models.TextField(blank=True, db_column='GA3', null=True)),
                ('visitors', models.IntegerField(blank=True, db_column='Visitors', null=True)),
                ('cv', models.IntegerField(blank=True, db_column='CV', null=True)),
                ('cvr', models.FloatField(blank=True, db_column='CVR', null=True)),
                ('profit', models.IntegerField(blank=True, db_column='Profit', null=True)),
                ('unitprice', models.IntegerField(blank=True, db_column='UnitPrice', null=True)),
                ('sourcetype', models.CharField(blank=True, db_column='SourceType', max_length=45, null=True)),
                ('sourcesubtype', models.CharField(blank=True, db_column='SourceSubType', max_length=45, null=True)),
                ('clientname', models.CharField(blank=True, db_column='ClientName', max_length=45, null=True)),
                ('productname', models.TextField(blank=True, db_column='ProductName', null=True)),
                ('accountname', models.TextField(blank=True, db_column='AccountName', null=True)),
            ],
            options={
                'db_table': 'cros_web',
                'managed': False,
            },
        ),
    ]
