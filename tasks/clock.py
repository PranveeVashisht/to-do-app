import requests
from .models import Project
from apscheduler.schedulers.background import BackgroundScheduler

count =0
def fetch_data():
    """
    Fetch data periodically using Github API and store in database
    """
    response = requests.get("https://api.github.com/orgs/Servatom/repos")
    data = response.json()
    global count
    count+=1
    print(count)
    for repo in data:
        Project.objects.get_or_create(
            title = repo['name'],
            url = repo['html_url']
        )
    
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_data, 'interval', seconds=120)
    scheduler.start()