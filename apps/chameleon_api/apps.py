from django.apps import AppConfig


class ChameleonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.chameleon_api"

    def ready(self):
        import apps.chameleon_api.signals
