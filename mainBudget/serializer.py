from rest_framework import serializers
from .models import mainBudget

class mainBudgetSerializer(serializers.ModelSerializer):

        class Meta:
            model = mainBudget
            fields = '__all__'
