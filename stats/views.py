from django.shortcuts import render
from .models import Stats
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .serializers import StatsSerializer
import json
import redis

from datetime import datetime as dt
# Create your views here.
import random
from rest_framework.decorators import api_view
from .services import convert_datetime_to_str, convert_str_to_datetime, get_gpu_usage, get_ram_usage, get_cpu_usage


@api_view(['GET', 'POST'])
def CurrentStats(request):
    if request.method == 'POST':
        available_usage_types = ['CPU','RAM','GPU']
        data = JSONParser().parse(request)
        req_usage_types = data['usage_types'].split(',')

        if all([req_usage_type in available_usage_types for req_usage_type in req_usage_types]):

                new_entry = Stats(time=dt.now(), request_method=request.method)
                if "CPU" in req_usage_types:
                    new_entry.cpu_usage = get_cpu_usage()
                if "RAM" in req_usage_types:
                    new_entry.ram_usage = get_ram_usage()
                if "GPU" in req_usage_types:
                    new_entry.gpu_usage = get_gpu_usage()
                new_entry.save()
                serializer = StatsSerializer(new_entry)
                print(serializer.data)
                return Response(serializer.data)
        return JsonResponse({'error':'You did not provide proper usage types'}, status=400)

    else: #GET request
        new_entry = Stats.objects.create(cpu_usage=get_cpu_usage(), ram_usage=get_ram_usage(), gpu_usage=get_gpu_usage(), time=dt.now(), request_method=request.method)
        serializer = StatsSerializer(new_entry)
        print(serializer.data)
        return Response(serializer.data)

def HistoryStats(request):
        all_stats_list = []
        stats_query = Stats.objects.all()
        for entry in stats_query:
            entry_dict = {}
            entry_dict[convert_datetime_to_str(entry.time)] = f"{entry.request_method}; CPU:{entry.cpu_usage}, RAM:{entry.ram_usage}, GPU:{entry.gpu_usage}"
            all_stats_list.append(entry_dict)
        return JsonResponse(all_stats_list, safe=False)

@api_view(['GET', 'POST'])
def ClearStats(request):
    if request.method == "POST":
        if request.data.get("time_from") != None and request.data.get("time_to") != None:
            data = JSONParser().parse(request)
            range_from = data['range_from']
            range_to = data['range_to']
            if range_from and range_to:
                dt_from = convert_str_to_datetime(range_from)
                dt_to = convert_str_to_datetime(range_to)
                entries = Stats.objects.filter(time__gte=dt_from,time__lte=dt_to)
                count = len(entries)
                entries.delete()
                return JsonResponse({'message': f'{count} entries have been deleted'}, status=204)
        else:
            entries = Stats.objects.all()
            count = len(entries)
            return JsonResponse({'message': f'{count} entries have been deleted'}, status=204)


# {
#     "range_from":"06:24:12:50:47",
#     "range_to":"06:24:15:56:47"
 # }

# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)

def redis_view():
    pass