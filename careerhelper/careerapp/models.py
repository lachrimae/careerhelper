from django.db import models

# Create your models here.

class Scale(models.Model):
    code = models.CharField(primary_key=True)
    name = models.CharField()
    min = models.IntegerField()
    max = models.IntegerField()

class JobRaw(models.Model):
    code = models.CharField(primary_key=True)
    title = models.CharField()
    description = models.CharField()

class JobGroup(models.Model):
    code = models.CharField(primary_key=True)
    name = models.CharField()

class Job(JobRaw):
    majorgroup = models.ForeignKey('JobGroup')
    minorgroup = models.ForeignKey('JobGroup')
    broadgroup = models.ForeignKey('JobGroup')

    def evalgroups():
        self.majorgroup = getmajorgroup()
        self.minorgroup = getminorgroup()
        self.broadgroup = getbroadgroup()
        self.save()

    def getmajorgroup():
        return JobGroup.get(code=(self.code[:2] + "-0000"))

    def getminorgroup():
        return JobGroup.get(code=(self.code[:4] + "000"))

    def getbroadgroup():
        return 

class EducationRaw(models.Model):
    code = models.CharField(primary_key=True)
    title = models.CharField()
    description = models.CharField()
    crosscode = ??????

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
    education = models.ForeignKey('Education')
    n = models.ForeignKey('MindsumoSample') 

class JobRelation(models.Model):
    job = models.ForeignKey('Job')
    relatedJob = models.ForeignKey('Job')
