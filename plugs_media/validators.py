"""
Plugs Media Validators
"""

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

from plugs_media.models import Media

# pylint: disable=R0903
class MediaValidator(object):
    """
    Validates if a string passed to a field
    accepting media resources is in fact a media
    resource
    """

    message = _('This field must be a valid media resource.')
    code = 'invalid_media'

    def __call__(self, value):
        try:
            Media.objects.get(file=value)
        except ObjectDoesNotExist:
            raise ValidationError(self.message, code=self.code)
