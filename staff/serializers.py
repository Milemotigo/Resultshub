from rest_framework import serializers
from .models import Staff


class staffSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Staff
        fields = '__all__'