# Generated by Django 2.1.7 on 2019-03-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]
