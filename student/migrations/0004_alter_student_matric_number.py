# Generated by Django 5.0.2 on 2024-03-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='matric_number',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]