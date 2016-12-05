from rest_framework import serializers
from .models import budzetMax

class budzetSerializer(serializers.ModelSerializer):

        class Meta:
            model = budzetMax
            fields = '__all__'
