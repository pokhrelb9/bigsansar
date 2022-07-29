from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bigsansar.contrib.account'
    verbose_name = 'Advance Information'

    def ready(self):
        import bigsansar.contrib.account.signals