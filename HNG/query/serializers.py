from rest_framework import serializers
from .models import User
class QueryParametersSerializer(serializers.Serializer):
    slack_name = serializers.CharField()
    track = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"