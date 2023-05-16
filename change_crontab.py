#Нужно установить python-crontab, не crontab!!!!!

import sys
from crontab import CronTab

time = sys.argv[1]                          # Без пробелов!

times = time.split(",")

my_cron = CronTab(user="OrangePI"                  # Username!
for job in my_cron:
    if job.comment == "send_report":
        my_cron.remove(job)
        my_cron.write()

for i in range(len(times)):
    minute = times[i][times[i].find(":") + 1 : ]
    hour = times[i][ : times[i].find(":")]

    my_cron = CronTab(user="OrangePI")                          # Username!
    job = my_cron.new(command="python3 send_report.py", comment="send_report")       # Путь до send_report.py !!!!!!!!!!
    job.minute.on(int(minute))
    job.hour.on(int(hour)) 
    my_cron.write()



