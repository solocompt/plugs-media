"""
Plugs media models
"""

from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from plugs_core import mixins

class Media(mixins.Timestampable, models.Model):
    """
    Media Model
    """
    name = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(max_length=255, upload_to='%Y/%m/%d/')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    # pylint: disable=R0903
    class Meta:
        """
        Metaclass definition
        """
        verbose_name = 'media'
        verbose_name_plural = 'media'
