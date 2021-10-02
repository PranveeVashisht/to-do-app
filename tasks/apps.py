from django.apps import AppConfig


class TasksConfig(AppConfig):
    name = "tasks"

    def ready(self):
        from . import cron

        cron.create_sample_tasks()
