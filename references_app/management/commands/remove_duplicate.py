# # your_app/management/commands/remove_duplicates.py
# from django.core.management.base import BaseCommand
# from django.db import transaction
# from django.db.models import Count
# from ...models import Soato

# class Command(BaseCommand):
#     help = 'Remove duplicate entries from the Soato table'

#     def handle(self, *args, **kwargs):
#         with transaction.atomic():
#             # Find duplicates based on unique fields (adjust these fields based on your model)
#             duplicates = (
#                 Soato.objects
#                 .values('version', 'code', 's_create', 'name_ru', 's_user_id', 'parent_code')
#                 .annotate(count= Count('id'))
#                 .filter(count__gt=1)
#             )

#             for duplicate in duplicates:
#                 # Keep the first occurrence and delete the rest
#                 duplicate_entries = Soato.objects.filter(
#                     version=duplicate['version'],
#                     code=duplicate['code'],
#                     s_create=duplicate['s_create'],
#                     name_ru=duplicate['name_ru'],
#                     s_user_id=duplicate['s_user_id'],
#                     parent_code=duplicate['parent_code']
#                 ).order_by('id')

#                 # Keep the first entry, delete the rest
#                 for entry in duplicate_entries[1:]:
#                     entry.delete()

#         self.stdout.write(self.style.SUCCESS('Successfully removed duplicate entries'))