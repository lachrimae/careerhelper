from django.db import models

# Create your models here.

class Scale(models.Model):
    """
    This is the scale that any `JobRating` will be in terms of.
    """
    code = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(max_length=100)
    min = models.IntegerField()
    max = models.IntegerField()

class SOCEntity(models.Model):
    """
    This class covers `MajorGroup`s, `MinorGroups`, `BroadGroups`,
    and `Job`s. They inherit the same basic indexing system. The
    `isa{}` functions allow for an ambiguous `SOCEntity` to
    self-identify. This was chosen rather than nested inheritance
    (Job <= BroadGroup <= MinorGroup <= MajorGroup <= SOCENntity)
    because it is more harmful (e.g.) for `Job`s to be members of
    the `MajorGroup` table than for us to have the somewhat unwieldy
    apparatus in this class. 
    _{}ID and {}_code functions are defined for entities which lack
    those qualities (e.g. each `MajorGroup` has a `_broadID`
    attribute, but any inappropriate calls will throw a RuntimeError.
    """
    code = models.CharField(primary_key=True, max_length=7)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default='')

    def isaMajorGroup(self):
        return self.code[-4:] == "0000"
    def isaMinorGroup(self):
        aboveBroad = self.code[-3:] == "000"
        notMajor = not self.isaMajorGroup()
        return aboveBroad and notMajor
    def isaBroadGroup(self):
        aboveJob = self.code[-1:] == "0"
        notMinor = not self.isaMinorGroup()
        notMajor = not self.isaMajorGroup()
        return aboveJob and notMinor and notMajor
    def isaJob(self):
        notBroad = not self.isaBroadGroup()
        notMinor = not self.isaMinorGroup()
        notMajor = not self.isaMajorGroup()
        return notBroad and notMinor and notMajor

    # The _{SOCTYPE}ID interfaces are for careful use, as they are 
    # liable to cause runtime errors if they are called for the wrong 
    # type of SOCEntity. the {SOCTYPE}_code interfaces don't need
    # exceptions written out because those are covered in their calls
    # to the _{SOCTYPE}ID functions.
    def __majorID(self):
        return self.code[:2]
    _majorID = property(__majorID)

    def __minorID(self):
        if self.isaMajorGroup():
            raise RuntimeError(
            "SOCEntity 'typing' is loosely managed. `minorID` has\n" +
            "been requested for a MajorGroup instance. This is\n" +
            "inadmissable.")
        return self.code[3]
    _minorID = property(__minorID)

    def __broadID(self):
        if self.isaMajorGroup() or self.isaMinorGroup:
            raise RuntimeError(
            "SOCEntity 'typing' is loosely managed. `broadID` has\n" +
            "been requested for a MajorGroup or MinorGroup\n" +
            "instance. This is inadmissable.")
        return self.code[4:6]
    _broadID = property(__broadID)

    # These functions are here for being used by the
    # `super_{}group` pk lookups in the subclasses of `SOCEntity`.
    # They exist so these non-nullable fields can be properly filled
    # during migrations.
    # It is absolutely recommended that the following usage is used
    # in lieu of these functions:
    # socentity.super_{}group.code
    def _majorgroup_code(self):
        return self._majorID + "-0000"
    def _minorgroup_code(self):
        return self._majorID + "-" + self._minorID + "000"
    def _broadgroup_code(self):
        return self._majorID + "-" + self._minorID + 
            self._broadID + "0" 


class MajorGroup(SOCEntity):
    pass

class MinorGroup(SOCEntity):
    super_majorgroup = models.ForeignKey('MajorGroup',
            default=self._majorgroup_code)

class BroadGroup(SOCEntity):
    super_majorgroup = models.ForeignKey('MajorGroup',
            default=self._majorgroup_code)
    super_minorgroup = models.ForeignKey('MinorGroup', 
            default=self._minorgroup_code)

class Job(SOCEntity):
    super_majorgroup = models.ForeignKey('MajorGroup',
            default=self._majorgroup_code)
    super_minorgroup = models.ForeignKey('MinorGroup', 
            default=self._minorgroup_code)
    super_broadgroup = models.ForeignKey('BroadGroup',
            default=self._broadgroup_code)

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
