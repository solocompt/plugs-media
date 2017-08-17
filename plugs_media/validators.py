"""
Plugs Media Validators
"""
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

from plugs_media.models import Media
from plugs_media.settings import plugs_media_settings

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
        # get the default medias
        try:
            if value in plugs_media_settings['DEFAULTS'].values():
                return
        except KeyError:
            pass
        # check if the media exists
        try:
            Media.objects.get(file=value)
        except ObjectDoesNotExist:
            raise ValidationError(self.message, code=self.code)

# pylint: disable=R0903
class MediaMaxSizeValidator(object):
    """
    Validates if file size does not exceeds the allowed limite
    """

    message = _('File size of {0} exceeds the allowed limit of {1}.')

    def __call__(self, value):
        if value.size > plugs_media_settings['MAX_FILE_SIZE']:
            raise ValidationError(self.message.format(
                value.size, plugs_media_settings['MAX_FILE_SIZE']))


# pylint: disable=R0903
class MediaContentTypeValidator(object):
    """
    Validates if file content type is allowed
    """

    message = _('File of type {0} not supported.')

    def __call__(self, value):
        if value.content_type not in plugs_media_settings['CONTENT_TYPES']:
            raise ValidationError(self.message.format(value.content_type))
