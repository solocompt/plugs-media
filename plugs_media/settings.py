"""
Plugs Media Settings
"""

from django.conf import settings

PROJECT_SETTINGS = getattr(settings, 'PLUGS_MEDIA', {})

DEFAULTS = {
    'CONTENT_TYPES': [
        'image/png',
        'image/jpeg',
        'image/gif',
        'application/pdf'
    ],
    'MAX_FILE_SIZE': 2000000
}

for setting in DEFAULTS.keys():
    if setting not in PROJECT_SETTINGS:
        PROJECT_SETTINGS[setting] = DEFAULTS[setting]

plugs_media_settings = PROJECT_SETTINGS
