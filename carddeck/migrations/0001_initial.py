# Generated by Django 3.2.6 on 2023-04-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('PlaceID', models.AutoField(primary_key=True, serialize=False)),
                ('PhotoPlace', models.CharField(max_length=500)),
                ('PlaceName', models.CharField(max_length=500)),
                ('PlaceLocation', models.CharField(max_length=500)),
                ('PlaceRate', models.FloatField(max_length=10)),
                ('PlacePrice', models.FloatField(max_length=10)),
            ],
        ),
    ]
