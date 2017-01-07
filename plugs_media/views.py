"""
Plugs Media Views
"""

from rest_framework import permissions

from plugs_core import viewsets

from plugs_media import models
from plugs_media import serializers


class MediaViewSet(viewsets.CreateReadViewSet):
    """
    Media Endpoint, does not support update
    or delete operations
    """
    queryset = models.Media.objects.all()
    serializer_class = serializers.MediaSerializer
    permission_classes = [permissions.IsAuthenticated]
