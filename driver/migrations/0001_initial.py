# Generated by Django 4.1.7 on 2023-05-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('bus_reg', models.CharField(max_length=200)),
                ('no_of_seats', models.CharField(max_length=200)),
                ('bus_type', models.CharField(max_length=200)),
                ('route', models.CharField(max_length=500)),
            ],
        ),
    ]
