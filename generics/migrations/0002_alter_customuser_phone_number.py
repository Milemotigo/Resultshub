# Generated by Django 5.0.2 on 2024-02-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
