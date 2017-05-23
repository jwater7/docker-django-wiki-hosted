# Add your own changes here -- but do not push to remote!!
# After changing the file, from root of repository execute:

# git update-index --assume-unchanged testproject/testproject/settings/local.py

#from .dev import *  # noqa @UnusedWildImport
from .base import *

# Adds static urls
DEBUG=True

# Access from anywhere
ALLOWED_HOSTS = ['*']

