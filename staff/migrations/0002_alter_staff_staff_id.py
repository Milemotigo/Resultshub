# Generated by Django 5.0 on 2024-02-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
