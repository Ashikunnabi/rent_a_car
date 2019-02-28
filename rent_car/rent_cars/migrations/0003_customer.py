# Generated by Django 2.1.7 on 2019-02-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_cars', '0002_carstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('present_address', models.CharField(max_length=200)),
            ],
        ),
    ]
