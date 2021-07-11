from django.apps import AppConfig


class TasksConfig(AppConfig):
    name = 'tasks'

    def ready(self):
        from . import clock
        clock.fetch_data()
        clock.start()