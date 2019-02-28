# Generated by Django 2.1.7 on 2019-02-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_cars', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('driving_licence_no', models.CharField(max_length=200)),
                ('present_address', models.CharField(max_length=200)),
                ('permanent_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='carstatus',
            name='car_status',
            field=models.CharField(choices=[('AB', 'Available'), ('OT', 'On Travel'), ('IS', 'In Service'), ('AB', 'Booked')], max_length=2),
        ),
    ]