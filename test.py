from time import sleep
import psutil
from datetime import datetime

# while True:
#     rambar = psutil.virtual_memory().percent
#     cpubar = psutil.cpu_percent()

#     print(f"RAM => {datetime.now()} {rambar}")
#     print(f"CPU => {datetime.now()} {cpubar}")
#     print('-' * 50)

    # sleep(1)

# for proc in psutil.process_iter(['pid', 'name', 'username', 'cmdline']):
    
#     with open("usage.txt", 'a') as f:
#         f.write(f"{proc.info} \n")

# ['pid', 'memory_percent', 'name', 'cmdline', 'cpu_times',
#             'create_time', 'memory_info', 'status', 'nice', 'username']



cpubar = psutil.cpu_times()
print(cpubar)

# {
#     'status': 'running',
#     'cmdline': ['python', 'main.py'],
#     'username': 'vada',
#     'pid': 22825,
#     'memory_percent': 0.17525542360923899,
#     'memory_info': pmem(rss=14458880, vms=34480128, shared=7852032, text=2830336, lib=0, data=8642560, dirty=0),
#     'create_time': 1679639505.02,
#     'nice': 0,
#     'name': 'python',
#     'cpu_times': pcputimes(user=0.07, system=0.02, children_user=0.0, children_system=0.0, iowait=0.0)
# }

conn.execute(f"""INSERT INTO USAGE (PID, NAME, SNAP_TIME, MEMORY, COMMAND, CPU, USERNAME) VALUES {values}""")