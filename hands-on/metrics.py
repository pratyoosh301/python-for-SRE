import psutil
import socket
from datetime import datetime
from pathlib import Path
import json

desktop = Path.home() / "Desktop"
log_file = desktop / "metric.log"

hostname = socket.gethostname()

cpu_threshhold =  0
ram_threshold = 80
disk_threshhold = 80

cpu=psutil.cpu_percent(interval=1)
ram=psutil.virtual_memory().percent
disk=psutil.disk_usage('/').percent

status = "ok"

if cpu>cpu_threshhold or disk>disk_threshhold or ram>ram_threshold:
    status = "not ok"
result = {
    "host": hostname,
    "cpu": cpu,
    "ram": ram,
    "disk": disk,
    "status": status,
}
   

with open('log_file', "a") as f:
    f.write(json.dumps(result) + "\n")