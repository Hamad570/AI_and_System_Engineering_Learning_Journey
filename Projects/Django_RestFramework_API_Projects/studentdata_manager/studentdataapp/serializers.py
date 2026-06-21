from rest_framework import serializers
from .models import studentdata

class studentserializers(serializers.ModelSerializer):
    class Meta:
        model=studentdata
        fields='__all__'