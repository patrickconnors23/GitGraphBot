import os, subprocess, sys
from crontab import CronTab

dirPath = os.path.dirname(os.path.abspath(__file__))

python3 = subprocess.check_output(["which", "python3"]).decode('utf-8').strip()

cron = CronTab(user='patrickconnors')

job = cron.new(command=f"cd {dirPath}; {python3} main.py")  
job.minute.every(1)

cron.write()  