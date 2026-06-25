from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Candidate, Block

class CandidateSerializer(serializers.ModelSerializer):
    updated_by_username = serializers.CharField(source='last_updated_by.username', read_only=True)

    class Meta:
        model = Candidate
        fields = ['id', 'name', 'party_name', 'vote_count', 'updated_by_username']  # 'party_name' must be here
        read_only_fields = ['vote_count', 'updated_by_username']

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'