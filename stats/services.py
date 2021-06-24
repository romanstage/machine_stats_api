import psutil
import GPUtil
from datetime import datetime as dt

def convert_datetime_to_str(dt_date):
    "converts datetime to string format MM:DD:hh:mm:ss"
    output = dt_date.strftime("%m:%d:%H:%M:%S")
    return output

def convert_str_to_datetime(str_date):
    "converts string format of (MM:DD:hh:mm:ss) to datetime obj"
    output = dt.strptime(str_date, "%m:%d:%H:%M:%S")
    output = output.replace(year=dt.now().year)
    return output

def get_cpu_usage():
    """Returns cpu load in percent format"""
    return [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()][0]

def get_ram_usage():
    """Returns ram load in percent format"""
    return psutil.virtual_memory().percent

def get_gpu_usage():
    """Return gpu load in percent format if GPU found, else None"""
    try:
        GPUs = GPUtil.getGPUs()
        if GPUs != []:
            return GPUs[0].load
    except:
        return None
