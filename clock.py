import json, requests
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

def my_scheduled_job():
    """Function to fetch json data from github api periodically"""
    response = requests.get("https://api.github.com/orgs/Servatom/repos")
    with open("tasks/api.json", mode='w') as file:
        json.dump(response.json(), file)

sched.add_job(my_scheduled_job, 'interval', minutes=2)
sched.start()