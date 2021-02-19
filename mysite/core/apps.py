from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'mysite.core'
    def ready(self):
        import mysite.core.signals  
