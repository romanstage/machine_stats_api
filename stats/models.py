from django.db import models


# class CPU_usage(models.Model):
#     usage = models.IntegerField()
#     time = models.DateTimeField(auto_now_add=True)
#     request_method = models.CharField(max_length=10, null=True, blank=True) #make choice field instead
#
#     def __str__(self):
#         return f"time: {self.time}; usage:{self.usage}; request_type:{self.request_type}"
#



class Stats(models.Model):
    cpu_usage = models.IntegerField(null=True, blank=True)
    ram_usage = models.IntegerField(null=True, blank=True)
    gpu_usage = models.IntegerField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    request_method = models.CharField(max_length=10, null=True, blank=True) #make choice field instead

    def __str__(self):
        return f"time: {self.time}; request_type:{self.request_method}"
