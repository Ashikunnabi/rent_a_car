# Generated by Django 2.1.7 on 2019-02-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_cars', '0004_auto_20190226_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=20)),
                ('distance_from_dhaka', models.CharField(max_length=20)),
            ],
        ),
    ]
