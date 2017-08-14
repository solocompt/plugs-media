"""
Plugs media models
"""

import uuid

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
    media_content_type = models.ForeignKey('MediaContentType', on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            parts = self.file.name.split('.')
            num = len(parts) - 1
            extension = '.' + parts[num]
            del parts[num]
            name = ''.join(map(str, parts))
            self.file.name = str(uuid.uuid4()) + extension
            self.name = name
        super(Media, self).save(*args, **kwargs)

    # pylint: disable=R0903
    class Meta:
        """
        Metaclass definition
        """
        verbose_name = 'media'
        verbose_name_plural = 'media'


class MediaContentType(mixins.Timestampable):
    """
    Media Content Type Model
    """
    id = models.CharField(max_length=201, primary_key=True)
    app_label = models.CharField(max_length=100, null=False, blank=False)
    model = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.id

    # pylint: disable=R0903
    class Meta:
        """
        Metaclass definition
        """
        verbose_name = 'media_content_type'
        verbose_name_plural = 'media_content_types'
