from .base import *


DEBUG = bool(config("DEBUG"))

IS_ENV = 'DEV'

ALLOWED_HOSTS = ['localhost','127.0.0.1', '']

INSTALLED_APPS += ['debug_toolbar',]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

#Database
# CONFIG_DIR = os.path.join(BASE_DIR, 'config/')
# parser = configparser.ConfigParser()
# parser.read_file(open(os.path.join(CONFIG_DIR, 'app.ini')))

#Done with postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': parser.get('hospital_dev', 'HP_DB_NAME'),
#         'USER': parser.get('hospital_dev', 'HP_DB_USER'),
#         'PASSWORD': parser.get('hospital_dev', 'HP_DB_PASSWORD'),
#         'HOST': parser.get('hospital_dev', 'HP_DB_HOST') or '127.0.0.1',
#         'PORT': parser.getint('hospital_dev', 'HP_DB_PORT') or '5432',

#     }
# }

# DEBUG TOOLBAR SETTINGS
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

print("\n")
print("DEBUG = ", DEBUG)
print("MODE = ", IS_ENV)
# print("DATABASES = ", DATABASES['default']['ENGINE'])
# print("HOST = ", DATABASES['default']['NAME'])
print("TEMPLATES = ", TEMPLATES[0]['DIRS'])
print("STATIC_ROOT = ", STATIC_ROOT)
print("MEDIA_ROOT = ", MEDIA_ROOT)
print("\n")