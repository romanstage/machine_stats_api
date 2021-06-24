from rest_framework import serializers
from stats.models import Stats
from .services import convert_str_to_datetime, convert_datetime_to_str

class StatsSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format="%m:%d:%H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Stats
        exclude = ('id', )
