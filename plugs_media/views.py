"""
Plugs Media Views
"""
from django.contrib.contenttypes.models import ContentType

from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from plugs_core import viewsets

from plugs_media import models
from plugs_media import serializers

from plugs_filter.decorators import auto_filters

@auto_filters
class MediaViewSet(viewsets.CreateReadViewSet):
    """
    Media Endpoint, does not support update
    or delete operations
    """
    queryset = models.Media.objects.all()
    serializer_class = serializers.MediaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    auto_filters_fields = ('content_type', 'object_id')

class MediaContentTypeViewSet(ReadOnlyModelViewSet):
    """
    Exposing Content Types
    """
    queryset = ContentType.objects.all()
    serializer_class = serializers.MediaContentTypeSerializer
    permission_classes = [permissions.AllowAny]
