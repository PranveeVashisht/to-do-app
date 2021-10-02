import os
from tasks.models import Task

def create_sample_tasks():
    os.chdir('tasks/sample_tasks')
    for file in os.listdir():
        if file.endswith('.txt'):
            with open(file, 'r') as f:
                task_text = f.read()
                Task.objects.update_or_create(title=task_text)
    os.chdir('../..')