# Generated by Django 5.0 on 2024-02-24 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('college', '0002_alter_college_college_name_alter_college_pobox_pmb_and_more'),
        ('staff', '0002_alter_staff_staff_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='College',
            new_name='Colleges',
        ),
    ]
