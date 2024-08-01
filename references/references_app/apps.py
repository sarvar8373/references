from django.apps import AppConfig


class ReferencesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'references_app'
    def ready(self):
        from django.core.management import call_command
        try:
            call_command('import_soato') 
        except Exception as e:
            print(f'Error running command: {e}')