from django.apps import AppConfig


class SheriffyConfig(AppConfig):
    name = 'sheriffy'


    def ready(self):
        import sheriffy.signals