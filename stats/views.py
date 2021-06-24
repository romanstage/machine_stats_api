from django.shortcuts import render
from .models import CPU_usage
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .serializers import CPU_usageSerializer

from datetime import datetime as dt
# Create your views here.
import random
from rest_framework.decorators import api_view

def get_cpu_usage():
    return random.randint(800,1200)


@api_view(['GET', 'POST'])
def CurrentStats(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        usage_types = data['usage_types']
        if "CPU" in usage_types:
            new_entry = CPU_usage.objects.create(usage=get_cpu_usage(), time=dt.now(), request_method=request.method)
            serializer = CPU_usageSerializer(new_entry)
            print(serializer.data)
            return Response(serializer.data)
        return JsonResponse({'error':'You did not provide proper usage stats'}, status=400)

    else: #GET request
        new_entry = CPU_usage.objects.create(usage=get_cpu_usage(), time=dt.now(), request_method=request.method)
        serializer = CPU_usageSerializer(new_entry)
        print(serializer.data)
        return Response(serializer.data)





