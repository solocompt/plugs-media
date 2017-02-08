from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers

from plugs_media.models import Media


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
        model = Media
        fields = ('id', 'name', 'file', 'content_type', 'object_id', 'user', 'created', 'updated')
        read_only_fields = ('user', )

class MediaContentTypeSerializer(serializers.ModelSerializer):
    """
    Media Serializer
    """

    class Meta:
        model = ContentType
        fields = ('id', 'app_label', 'model')
