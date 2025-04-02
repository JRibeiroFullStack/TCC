from django.apps import AppConfig

class SensoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sensores'

    def ready(self):
        from sensores.threadings import start_coleta_dados

        start_coleta_dados()