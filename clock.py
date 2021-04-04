from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour = '6-0', minute='*/20')
def scheduled_job():
    url = https://bdmaster2021.herokuapp.com/callback
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)

sched.start()
