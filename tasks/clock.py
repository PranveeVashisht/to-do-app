import json, requests
# from apscheduler.schedulers.blocking import BlockingScheduler
# sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=3)
def my_scheduled_job():
    """Function to fetch json data from github api periodically"""
    response = requests.get("https://api.github.com/users/rdotjain/repos")
    with open("api.json", mode='w') as file:
        json.dump(response.json(), file)

# sched.start()
my_scheduled_job()