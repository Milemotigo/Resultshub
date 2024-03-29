# Generated by Django 5.0 on 2024-02-23 15:31

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('college', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(unique=True)),
                ('matric_number', models.CharField(max_length=50, unique=True)),
                ('profile_picture', models.ImageField(default='default_user_icon.png', upload_to='profile_picture/Students', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='college_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
