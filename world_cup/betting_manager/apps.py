from django.apps import AppConfig


class BettingManagerConfig(AppConfig):
    name = 'betting_manager'

    def ready(self):
        import betting_manager.signals