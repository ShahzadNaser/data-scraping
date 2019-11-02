from crontab import CronTab
cron = CronTab(user=True)

job = cron.new(command='python example1.py', comment='comment')
job.minute.every(1)

for item in cron:
    print(item)

job.clear()

for item in cron:
    print(item)

cron.write()
# job = cron.new(command='python Documents/cron.py')
# job.minute.every(1)
# cron.write()

#for item in cron:
    # cron.remove(item)
    # cron.write()


