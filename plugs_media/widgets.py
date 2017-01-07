"""
Media Widgets
"""

from django.conf import settings
from django.forms.widgets import ClearableFileInput

class MediaWidget(ClearableFileInput):
    """
    Media widget to deal with images
    """

    def render(self, name, value, attrs=None):
        output = super(MediaWidget, self).render(name, value, attrs)
        img_html = '<img src="{0}{1}"/><br/>'.format(settings.MEDIA_URL, value)
        return img_html + output
