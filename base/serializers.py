from django.contrib.auth.models import User
from rest_framework import serializers

from exam.serializers import TestpaperAssignSerializer

class UserSerializer(serializers.ModelSerializer):
    assignments = TestpaperAssignSerializer(source='testpaperassign_set', read_only=True, many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'assignments']