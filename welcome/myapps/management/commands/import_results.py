import pandas as pd
from django.core.management.base import BaseCommand
from myapps.models import Result

class Command(BaseCommand):
    help = 'Import student results from Excel'

    def handle(self, *args, **kwargs):

        file_path = "results.xlsx"

        data = pd.read_excel(file_path)

        for _, row in data.iterrows():
            Result.objects.create(
                student_name=row['student_name'],
                reg_no=row['reg_no'],
                design_marks=row['design_marks'],
                arvr_marks=row['arvr_marks'],
                bda_marks=row['bda_marks'],
                ethics_marks=row['ethics_marks'],
                iot_marks=row['iot_marks'],
                pom_marks=row['pom_marks'],
            )

        self.stdout.write(self.style.SUCCESS("Results Imported Successfully"))