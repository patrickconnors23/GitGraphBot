import os, subprocess, sys
from crontab import CronTab

# Get current directory`
dirPath = os.path.dirname(os.path.abspath(__file__))

# Get version of python to run
python3 = subprocess.check_output(["which", "python3"]).decode('utf-8').strip()
git = subprocess.check_output(["which", "git"]).decode('utf-8').strip()

# Init Crontab instance 
cron = CronTab(user='patrickconnors')

# Add command
job = cron.new(command=f"cd {dirPath}; {git} config --global -l")  
job.minute.every(1)
job = cron.new(command=f"cd {dirPath}; {python3} main.py")  
job.minute.every(1)

cron.write()  