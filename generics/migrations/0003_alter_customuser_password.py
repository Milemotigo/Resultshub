# Generated by Django 5.0.2 on 2024-02-29 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generics', '0002_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
