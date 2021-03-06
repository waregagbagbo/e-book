from django.apps import AppConfig


class BookdataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookdata'
    
    def ready(self):
        import bookdata.signals
