import csv
import os

from django.core.management.base import BaseCommand, CommandError

from careerapp.models import Job, BroadGroup, MinorGroup, MajorGroup

class Command(BaseCommand):
    help = 'Imports csv data from data/cooked/'

    def add_arguments(self, parser):
        parser.add_argument('dirpath', nargs=1, type=str)

    def __readdata(filepath):
        data = []
        csvfile = open(filepath)
        try:
            datareader = csv.reader(csvfile, delimiter=',', quotechar='"')

            firstRow = next(datareader)
            headerCol1 = firstRow[0]
            headerCol2 = firstRow[1]

            for row in datareader:
                data.append({headerCol1: row[0], headerCol2: row[1]})
        finally:
            csvfile.close()

        return data
    
    def handle(self, *args, **options):
        dirpath = options['dirpath']
        majorpath = os.path.join(dirpath, 'major_groups.csv')
        minorpath = os.path.join(dirpath, 'minor_groups.csv')
        broadpath = os.path.join(dirpath, 'broad_groups.csv')
        occuppath = os.path.join(dirpath, 'detailed_occupations.csv')

        majorgroups = self.__readdata(majorpath)
        for mg in majorgroups:
            mgi = MajorGroup(code=mg['SOC Code'], title=mg['Title'])
            mgi.save()

        minorgroups = self.__readdata(minorpath)
        for mg in minorgroups:
            code = mg['SOC Code']
            title = mg['Title']
            mgi = MinorGroup(code=code, title=title,
                    super_majorgroup=MajorGroup.objects.get(
                        _majorID=code[:2]))
            mgi.save()

        broadgroups = self.__readdata(broadpath)
        for bg in broadgroups:
            code = bg['SOC Code']
            title = bg['Title']
            bgi = BroadGroup(code=code, title=title,
                    super_majorgroup=MajorGroup.objects.get(
                        _majorID=code[:2]),
                    super_minorgroup=MinorGroup.objects.get(
                        _minorID=code[3]))
            bgi.save()

        jobs = self.__readdata(occuppath)
        for job in jobs:
            code = job['SOC Code']
            title = job['Title']
            jobi = Job(code=code, title=title,
                    super_majorgroup=MajorGroup.objects.get(
                        _majorID=code[:2]),
                    super_minorgroup=MinorGroup.objects.get(
                        _minorID=code[3]),
                    super_broadgroup=BroadGroup.objects.get(
                        _broadID=code[4:6]))
            jobi.save()
