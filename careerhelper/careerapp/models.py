from django.db import models

# Create your models here.

class Scale(models.Model):
    code = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(max_length=100)
    min = models.IntegerField()
    max = models.IntegerField()

class SOCEntity(models.Model):
    code = models.CharField(primary_key=True, max_length=7)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

class JobGroup(SOCEntity):
    def isaMajorGroup():
        return code[-4:] == "0000"
    def isaMinorGroup():
        return code[-3:] == "000"
    def isaBroadGroup():
        return code[-1:] == "0"

class MajorGroup(JobGroup):
    pass

class MinorGroup(JobGroup):
    super_majorgroup = models.ForeignKey('MajorGroup')

class BroadGroup(JobGroup):
    super_minorgroup = models.ForeignKey('MinorGroup')

class Job(SOCEntity):
    super_broadgroup = models.ForeignKey('BroadGroup')

class EducationRaw(models.Model):
    code = models.CharField(primary_key=True, max_length=7)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    #crosscode = ?????? #determine this if needed

class WorkerQuality(models.Model):
    code = models.CharField(primary_key=True, max_length=9)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class JobRating(models.Model):
    job = models.ForeignKey('Job')
    quality = models.ForeignKey('WorkerQuality')
    scale = models.ForeignKey('Scale')
    value = models.FloatField()
    n = models.IntegerField()
    lowerbound = models.FloatField()
    upperbound = models.FloatField()
    suppress = models.BooleanField()
    irrelevant = models.BooleanField()

class MindsumoSample(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    
class MindsumoCellRaw(models.Model):
    jobcode = models.ForeignKey('Job')
    sample = models.ForeignKey('MindsumoSample')
    education = models.ForeignKey('EducationRaw')
    n = models.IntegerField()

class JobRelation(models.Model):
    job = models.ForeignKey('Job')
    relatedJob = models.ForeignKey('Job', related_name='related_job')
