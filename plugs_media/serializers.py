from magic import Magic

from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile

from base64 import b64decode

from rest_framework import serializers

from plugs_media import models
from plugs_media import validators


class HybridFileFieldSerializer(serializers.FileField):

    def get_content_type(self, file_):
        """
        Returns the content type of the file using python magic
        """
        magic = Magic(mime=True)
        return magic.from_buffer(file_.read(1024))

    def to_base64(self, data):
        try:
            # we are discarding the data uri if present
            data = data.split(',')[1]
        except:
            pass
        file_ = BytesIO(b64decode(data))
        content_type = self.get_content_type(file_)
        extension = content_type.split('/')[1]
        return InMemoryUploadedFile(file_, None, extension, content_type, file_.__sizeof__(), None)

    def to_internal_value(self, data):
        """
        This file field serializer can accept a binary file
        or a base64 encoded string with the contents of a file
        """
        if not hasattr(data, 'file'):
            data = self.to_base64(data)
        return super().to_internal_value(data)


class MediaSerializer(serializers.ModelSerializer):
    """
    Media Serializer
    """

    file = HybridFileFieldSerializer(
        max_length=100,
        allow_empty_file=True,
        use_url=False,
        validators=[
            validators.MediaMaxSizeValidator(),
            validators.MediaContentTypeValidator(),
        ]
    )

    class Meta:
        model = models.Media
        fields = ('id', 'name', 'user', 'file', 'created', 'updated')
        read_only_fields = ('user', )
