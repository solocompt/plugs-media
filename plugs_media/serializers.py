from rest_framework import serializers

from plugs_media import models


class MediaSerializer(serializers.ModelSerializer):
    """
    Media Serializer
    """

    file = serializers.FileField(
        max_length=100,
        allow_empty_file=False,
        use_url=False
    )

    class Meta:
        model = models.Media
        fields = ('id', 'name', 'user', 'file', 'created', 'updated')
        read_only_fields = ('user', )
