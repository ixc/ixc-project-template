"""
Rename to ``local.py`` and update to suit the local environment.
"""

import os

# ENVIRONMENT #################################################################

# These environment variables are injected into the base settings module and
# used to derive other settings.

os.environ.setdefault('BASE_SETTINGS_MODULE', 'develop')

from .calculated import *

# SECRETS #####################################################################

# Do not commit secrets to VCS. Get from https://interaction.1password.com

# DATABASES['default']['PASSWORD'] = ''
EMAIL_HOST_PASSWORD = ''
# MASTER_PASSWORD = ''
RAVEN_CONFIG['dsn'] = ''

# OVERRIDE ####################################################################

# Only add true local-only and temporary override settings here. Anything else
# should go in an environment specific settings module.
