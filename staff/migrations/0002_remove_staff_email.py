# Generated by Django 5.0.2 on 2024-02-16 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='email',
        ),
    ]