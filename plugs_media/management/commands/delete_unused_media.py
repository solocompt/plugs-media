import os

from django.core.management.base import BaseCommand
from django.apps import apps
from django.conf import settings

from plugs_media.fields import MediaField
from plugs_media.models import Media

class Command(BaseCommand):

    help = "Delete unused media files and media records which have no reference in models."

    media_root = settings.MEDIA_ROOT

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run', action='store_true', dest='dry_run',
            help="Just show what files would be deleted; do not actually delete them.",
        )

    def dry_run(self):
        count_files = len(self._get_unused_media_files())
        count_records = len(self._get_unused_media_records())
        msg = 'A total of {0} files and of {1} records would be deleted.'.format(count_files, count_records)
        self.stdout.write(self.style.SUCCESS(msg))

    def handle(self, *args, **options):
        if options['dry_run']:
            self.dry_run()
        else:
            count_files = self._delete_unused_media_files()
            count_records = self._delete_unused_media_records()
            msg = 'deleted files: {0} deleted records: {1}'.format(count_files, count_records[0])
            self.stdout.write(self.style.SUCCESS(msg))

    def _get_all_media(self):
        """
        Get all media in filesystem
        """
        media = []

        for root, dirs, files in os.walk(self.media_root):
            for name in files:
                abs_path = os.path.join(root, name)
                path = os.path.relpath(abs_path, self.media_root)
                # does not remove files inside default folder
                if not path.startswith('default'):
                    media.append(path)
        return media

    def _get_media_fields(self):
        """
        Get all MediaFields
        """
        all_models = apps.get_models()
        fields = []

        for model in all_models:
            for field in model._meta.get_fields():
                if isinstance(field, MediaField):
                    fields.append(field)

        return fields

    def _get_used_media(self):
        """
        Get media which are still used in models
        """

        media = []

        for field in self._get_media_fields():

            is_null = {'%s__isnull' % field.name: True,}
            is_empty = {'%s' % field.name: '',}

            for obj in field.model.objects.exclude(**is_empty).exclude(**is_null):
                media.append(getattr(obj, field.name))

        return media

    def _get_unused_media_files(self):
        all_media = self._get_all_media()
        used_media = self._get_used_media()
        return [x for x in all_media if x not in used_media]

    def _delete_unused_media_files(self):
        """
        Deletes unused media files
        """
        files = self._get_unused_media_files()
        counter = 0
        for file_ in files:
            try:
                file_ = self.media_root + file_
                os.remove(file_)
                counter += 1
            except FileNotFoundError:
                msg = 'Could not delete {0}'.format(file_)
                self.stdout.write(self.style.ERROR(msg))
        return counter


    def _get_unused_media_records(self):
        all_media = Media.objects.all().values_list('file', flat=True)
        used_media = self._get_used_media()
        return [x for x in all_media if x not in used_media]


    def _delete_unused_media_records(self):
        """
        Deletes stale records in media table
        """
        records = self._get_unused_media_records()
        return Media.objects.all().filter(file__in=records).delete()
