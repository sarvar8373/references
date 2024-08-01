# import pandas as pd
# from django.core.management.base import BaseCommand
# from django.conf import settings
# from ...models import NATION

# class Command(BaseCommand):
#     help = 'Load data from Excel file into the database'

#     def handle(self, *args, **kwargs):
#         file_path = settings.EXCEL_FILE_PATH

#         # Read the Excel file using pandas  
#         data = pd.read_excel(file_path)

#         # Iterate through the rows of the DataFrame
#         for index, row in data.iterrows():
#             NATION.objects.create(
#                 version=row['version'],
#                 s_comment=row['s_comment'],
#                 s_create=row['s_create'],
#                 s_status=row['s_status'],
#                 name_ru=row['name_ru'],
#                 name_uz=row['name_uz'],
#                 name_uzl=row['name_uzl'],
#                 s_user_id=row['s_user_id'],
#             )
#         self.stdout.write(self.style.SUCCESS('Successfully loaded data into the database'))
