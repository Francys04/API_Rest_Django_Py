"""This line imports the AppConfig class from the django.apps module. 
The AppConfig class is a base class for application configuration in Django."""
from django.apps import AppConfig

"""This defines a new subclass of AppConfig called ApiConfig. 
The class will be used to configure the behavior of the api Django app."""
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #  This is used to specify the primary key field type for models that do not explicitly define their own primary key field.
    name = 'api' # App's name is set to 'api'.
