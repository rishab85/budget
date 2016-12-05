from rest_framework import serializers
from .models import dueDates

class dueDatesSerializer(serializers.ModelSerializer):

        class Meta:
            model = dueDates
            fields = '__all__'
