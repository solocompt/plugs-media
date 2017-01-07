"""
Custom fields required by media
"""

from django.db import models

from plugs_media.widgets import MediaWidget
from plugs_media.validators import MediaValidator

class MediaField(models.CharField):
    """
    This field is a special charfield
    that accepts and stores chars but
    references a resource in the media model
    which for now are images
    """

    default_validators = [MediaValidator()]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 100
        super(MediaField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        """
        Using this to provide a custom widget
        in the admin site
        """
        kwargs['widget'] = MediaWidget
        return super(MediaField, self).formfield(**kwargs)
