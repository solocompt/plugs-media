"""
Plugs media models
"""

import uuid

from django.conf import settings
from django.db import models

from plugs_core import mixins

class Media(mixins.Timestampable, models.Model):
    """
    Media Model
    """
    name = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(max_length=255, upload_to='%Y/%m/%d/')
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
