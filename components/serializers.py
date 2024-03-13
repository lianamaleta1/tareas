from rest_framework import serializers
from .models import *

class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meta
        fields = ('orden','codigo','nombre','tipo','um','estado')