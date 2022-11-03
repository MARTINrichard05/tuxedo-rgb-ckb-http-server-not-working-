import psutil
import requests
from time import sleep
while True:
    try:
        cpu = psutil.cpu_percent(0.04)
        requests.get("http://127.0.0.1:6670/["+str(int(cpu*2))+",0,"+str(int(cpu*2))+"]")
    except :
        pass
    sleep(0.04)