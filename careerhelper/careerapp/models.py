from django.db import models

# Create your models here.

class Scale(models.Model):
    code = models.CharField(primary_key=True)
    name = models.CharField()
    min = models.IntegerField()
    max = models.IntegerField()

class SOCEntity(models.Model):
    code = models.CharField(primary_key=True)
    name = models.CharField()
    description = models.CharField()

class JobGroup(SOCEntity):
    def isaMajorGroup():
        return code[-4:] == "0000"
    def isaMinorGroup():
        return code[-3:] == "000"
    def isaBroadGroup():
        return code[-1:] == "0":
    pass

class MajorGroup(JobGroup):
    pass

class MinorGroup(JobGroup):
    majorgroup = models.ForeignKey('MajorGroup')

class BroadGroup(JobGroup):
    minorgroup = models.ForeignKey('MinorGroup')

class Job(SOCEntity):
    broadgroup = models.ForeignKey('BroadGroup')

class EducationRaw(models.Model):
    code = models.CharField(primary_key=True)
    title = models.CharField()
    description = models.CharField()
    #crosscode = ?????? #determine this if needed

class WorkerQuality(models.Model):
    code = models.CharField(primary_key=True)
    name = models.CharField()
    description = models.CharField()

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
    date = models.CharField()
    source = models.CharField()

class MindsumoSample(models.Model):
    name = models.CharField(primary_key=True)
    
class MindsumoCellRaw(models.Model):
    jobcode = models.ForeignKey('Job')
    sample = models.CharField()
    education = models.ForeignKey('EducationRaw')
    n = models.ForeignKey('MindsumoSample') 

class JobRelation(models.Model):
    job = models.ForeignKey('Job')
    relatedJob = models.ForeignKey('Job')
