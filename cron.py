import os
from crontab import CronTab

filePath = os.path.dirname(os.path.abspath(__file__))

python3 = "/Library/Frameworks/Python.framework/Versions/3.6/bin/python3"

cron = CronTab(user='patrickconnors')

job = cron.new(command=f"cd {filePath}; {python3} main.py")  
job.minute.every(1)

cron.write()  