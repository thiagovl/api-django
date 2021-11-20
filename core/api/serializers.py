from rest_framework import serializers

from django.contrib.auth.models import User, Group
from rest_framework import serializers

class ResumoSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, read_only=True)
    company = serializers.CharField(max_length=100)
    occupation = serializers.CharField(max_length=100)
    activities = serializers.CharField()
    tags = serializers.CharField()
    start_date = serializers.DateTimeField()
    departure_date = serializers.DateTimeField()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']