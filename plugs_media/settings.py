"""
Plugs Media Settings
"""

from django.conf import settings

PROJECT_SETTINGS = getattr(settings, 'PLUGS_MEDIA_DEFAULTS', {})
plugs_media_settings = PROJECT_SETTINGS
