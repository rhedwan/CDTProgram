from rest_framework import serializers

class QueryParametersSerializer(serializers.Serializer):
    slack_name = serializers.CharField()
    track = serializers.CharField()