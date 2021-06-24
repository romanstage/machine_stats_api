from django.db import models


class CPU_usage(models.Model):
    usage = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    request_method = models.CharField(max_length=10, null=True, blank=True) #make choice field instead

    def __str__(self):
        return f"time: {self.time}; usage:{self.usage}; request_type:{self.request_type}"
