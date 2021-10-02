from django.apps import AppConfig


class TasksConfig(AppConfig):
    name = 'tasks'

    def ready(self):
        print("Running")
        from . import cron
        cron.create_sample_tasks()