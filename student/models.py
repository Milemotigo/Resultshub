from django.db import models
from college.models import Department
from generics.models import CustomUser
from django.core.validators import FileExtensionValidator

STATE_CHOICES = (
    ('Abia Umuahia', 'Abia Umuahia'),
    ('Adamawa Yola', 'Adamawa Yola'),
    ('Akwa Ibom Uyo', 'Akwa Ibom Uyo'),
    ('Anambra Awka', 'Anambra Awka'),
    ('Bauchi Bauchi', 'Bauchi Bauchi'),
    ('Bayelsa Yenagoa', 'Bayelsa Yenagoa'),
    ('Benue Makurdi', 'Benue Makurdi'),
    ('Borno Maiduguri', 'Borno Maiduguri'),
    ('Cross River Calabar', 'Cross River Calabar'),
    ('Delta Asaba', 'Delta Asaba'),
    ('Ebonyi Abakaliki', 'Ebonyi Abakaliki'),
    ('Edo Benin City', 'Edo Benin City'),
    ('Ekiti Ado-Ekiti', 'Ekiti Ado-Ekiti'),
    ('Enugu Enugu', 'Enugu Enugu'),
    ('Gombe Gombe', 'Gombe Gombe'),
    ('Imo Owerri', 'Imo Owerri'),
    ('Jigawa Dutse', 'Jigawa Dutse'),
    ('Kaduna Kaduna', 'Kaduna Kaduna'),
    ('Kano Kano', 'Kano Kano'),
    ('Katsina Katsina', 'Katsina Katsina'),
    ('Kebbi Birnin Kebbi', 'Kebbi Birnin Kebbi'),
    ('Kogi Lokoja', 'Kogi Lokoja'),
    ('Kwara Ilorin', 'Kwara Ilorin'),
    ('Lagos Ikeja', 'Lagos Ikeja'),
    ('Nasarawa Lafia', 'Nasarawa Lafia'),
    ('Niger Minna', 'Niger Minna'),
    ('Ogun Abeokuta', 'Ogun Abeokuta'),
    ('Ondo Akure', 'Ondo Akure'),
    ('Osun Osogbo', 'Osun Osogbo'),
    ('Oyo Ibadan', 'Oyo Ibadan'),
    ('Plateau Jos', 'Plateau Jos'),
    ('Rivers Port Harcourt', 'Rivers Port Harcourt'),
    ('Sokoto Sokoto', 'Sokoto Sokoto'),
    ('Taraba Jalingo', 'Taraba Jalingo'),
    ('Yobe Damaturu', 'Yobe Damaturu'),
    ('Zamfara Gusau', 'Zamfara Gusau'),
    ('Federal Capital Territory Abuja', 'Federal Capital Territory Abuja')
)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    #department = models.ForeignKey(Department, on_delete=models.CASCADE
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=250, unique=False, null=True)
    last_name = models.CharField(max_length=250, unique=False, null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=300, default='Delta Asaba')
    city = models.CharField(max_length=200, null=True)
    zipcode = models.IntegerField(null=True)
    matric_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    #phone = models.IntegerField(default=0, unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture/students', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

