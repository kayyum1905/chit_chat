try:
    from .settings_base import *
except ImportError:
    pass

DEBUG = True

print('Development settings in use')
