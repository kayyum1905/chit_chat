try:
    from .settings_base import *
except ImportError:
    pass

DEBUG = False

print('Production settings in use')
