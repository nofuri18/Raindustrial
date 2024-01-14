# Generated by Django 4.2.8 on 2024-01-06 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nip',
            field=models.CharField(help_text='Enter 16 digits NIP number', max_length=16, unique=True, verbose_name='NIP Number'),
        ),
    ]
