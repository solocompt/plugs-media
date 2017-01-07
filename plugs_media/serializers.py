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
        fields = ('id', 'name', 'file', 'created', 'updated')
