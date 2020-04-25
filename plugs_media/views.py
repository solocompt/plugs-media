from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from plugs_core import viewsets

from plugs_media import models
from plugs_media import serializers
from plugs_media.permissions import IsOwnerOrReadOnly

class MediaViewSet(viewsets.CreateReadViewSet):
    queryset = models.Media.objects.all()
    serializer_class = serializers.MediaSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
