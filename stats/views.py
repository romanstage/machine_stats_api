from datetime import datetime as dt
import json
import redis

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.conf import settings

from .services import convert_datetime_to_str, convert_str_to_datetime, get_gpu_usage, get_ram_usage, get_cpu_usage


# Connect to Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)


@api_view(['GET', 'POST'])
def current(request):
    """Returns either all current stats or specified in requests body"""

    #returns all current stats
    if request.method == 'GET':
        key = convert_datetime_to_str(dt.now())
        value = f"{request.method}; CPU:{get_cpu_usage()}, RAM:{get_ram_usage()}, GPU:{get_gpu_usage()}"
        redis_instance.set(key, value)
        item = {key:value}
        return Response(item, status=200)

    #return requested current stats
    elif request.method == 'POST':
        data = json.loads(request.body)
        req_usage_types = data["usage_types"].split(',')
        available_usage_types = ['CPU', 'RAM', 'GPU']
        if all([req_usage_type in available_usage_types for req_usage_type in req_usage_types]):
            value = 'POST; '
            if "CPU" in req_usage_types:
                value += f"CPU:{get_cpu_usage()}; "
            if "RAM" in req_usage_types:
                value += f"RAM:{get_ram_usage()}; "
            if "GPU" in req_usage_types:
                value += f"GPU:{get_gpu_usage()}; "

            key = convert_datetime_to_str(dt.now())
            redis_instance.set(key, value)

            item = {key: value.rstrip()}
            return Response(item, 200)
        return JsonResponse({'error': 'You did not provide proper usage types'}, status=400)


@api_view(['GET'])
def history(request):
    """Return all history of stats along  with request type and time"""
    if request.method == 'GET':
        items = {}
        for key in redis_instance.keys("*"):
            items[key.decode("utf-8")] = redis_instance.get(key)

        return Response(items, status=200)


@api_view(['GET', 'POST'])
def clear(request):
    """Removes either all entries on withing specified range"""
    if request.method == 'POST':
        # delete in range
        if request.data.get("range_from",None) != None and request.data.get("range_to",None) != None:
            try:
                data = request.data
                range_from_dt = convert_str_to_datetime(data['range_from'])
                range_to_dt = convert_str_to_datetime(data['range_to'])

            except:
                return JsonResponse({'error': 'You did not provide proper date ranges'}, status=400)
            delete_count = 0
            for key in redis_instance.keys("*"):
                key_dt = convert_str_to_datetime(key.decode("utf-8"))
                if key_dt > range_from_dt and key_dt < range_to_dt:
                    result = redis_instance.delete(key)
                    if result == 1:
                        delete_count += 1

            return JsonResponse({'message': f'{delete_count} keys successfully deleted'}, status=204)

        #delete all
        else:
            redis_instance.flushdb();
            return JsonResponse({"message": "All keys have been deleted"}, status=204)
