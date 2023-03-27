import psutil
from datetime import datetime

from db import save_snapshot_to_db


class Usage:    
    def __init__(
        self,
        pid,
        name,
        snap_time,
        memory_percent,
        cmdline,
        cpu_percent,
        username,
    ):
        self.pid = pid
        self.name = name
        self.snap_time = snap_time
        self.memory_percent = memory_percent
        self.cmdline = cmdline
        self.cpu_percent = cpu_percent
        self.username = username

    def to_tuple(self):
        return (
            self.pid,
            self.name,
            self.snap_time,
            self.memory_percent,
            str(self.cmdline),
            self.cpu_percent,
            self.username
        )


def usage_snapshot(exclude):
    usage = []

    for proc in psutil.process_iter(['pid', 'memory_percent', 'name', 'cmdline',
             'create_time', 'memory_info', 'status', 'username']):
        proc.info['snap_time'] = str(datetime.now())
        proc.info['cpu_percent'] = "Undefined"

        if proc.name not in exclude:
            obj = Usage(
                proc.info['pid'],
                proc.info['name'],
                proc.info['snap_time'],
                proc.info['memory_percent'],
                proc.info['cmdline'],
                proc.info['cpu_percent'],
                proc.info['username'],
            )

            usage.append(obj)
    return usage
    

if __name__ == "__main__":
    exclude = ['chrome', 'code', 'bash']
    usage = usage_snapshot(exclude)    
    save_snapshot_to_db(usage)

