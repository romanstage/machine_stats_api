from rest_framework import serializers
from stats.models import CPU_usage

class CPU_usageSerializer(serializers.ModelSerializer):
    # created = serializers.ReadOnlyField()           #note we should not be able to change it
    # datecompleted = serializers.ReadOnlyField()     #note we should not be able to change it

    class Meta:
        model = CPU_usage
        fields = ['id','time','usage',]
