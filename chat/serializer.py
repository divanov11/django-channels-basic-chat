from attr import fields
from rest_framework import serializers
from . models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = pdf_details
        fields = '__all__'
