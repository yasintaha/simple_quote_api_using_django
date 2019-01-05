from rest_framework import serializers
from .models import Quote_model

class Quote_Serializer(serializers.ModelSerializer):
    class Meta():
        model = Quote_model
        fields = '__all__'
