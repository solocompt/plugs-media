"""
Plugs media models
"""

from django.db import models

from plugs_core import mixins

class Media(mixins.Timestampable, models.Model):
    """
    Media Model
    """
    name = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(max_length=255, upload_to='%Y/%m/%d/')


    # pylint: disable=R0903
    class Meta:
        """
        Metaclass definition
        """
        verbose_name = 'media'
        verbose_name_plural = 'media'
