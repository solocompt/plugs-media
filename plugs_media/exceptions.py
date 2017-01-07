"""
Media APP exceptions
"""
from django.utils.translation import ugettext as _

from rest_framework.exceptions import APIException
from rest_framework import status

class MediaException(APIException):
    """
    Exception raised when the creation of a media resource fails
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Could not create media resource.')
