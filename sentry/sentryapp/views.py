from django.shortcuts import render, HttpResponse
from datetime import datetime

import psutil

from sentryapp.models import UsageMonitor


def usage_snapshot():
    processes = psutil.process_iter(['pid', 'memory_percent', 
                                     'name', 'cmdline',
                                     'create_time', 'memory_info', 'status', 'username'])
    return processes


def home(request):
    exclude = ['code', 'chrome', 'bash']
    processes = usage_snapshot()
    data = []
    for proc in processes:
        if proc.info['name'] not in exclude:
            if not UsageMonitor.objects.filter(pid=proc.info['pid']).exists():
                usage = UsageMonitor(
                    pid=proc.info['pid'],
                    name=proc.info['name'],
                    snap_time=datetime.now(),
                    memory=round(proc.info['memory_percent'], 2),
                    command=str(proc.info['cmdline']),
                    cpu="undefined",
                    username=proc.info['username'],
                )
                usage.save()
                data.append(usage)
            else:
                usage = UsageMonitor.objects.get(pid=proc.info['pid'])
                usage.pid = proc.info['pid']
                usage.name = proc.info['name']
                usage.snap_time = datetime.now(),
                usage.memory = round(proc.info['memory_percent'], 2)
                usage.command = str(proc.info['cmdline'])
                usage.cpu = "undefined"
                usage.username = proc.info['username']
                usage.save()
                data.append(usage)

    context = {
        'data': data
        }
    return render(request, 'home.html', context)
