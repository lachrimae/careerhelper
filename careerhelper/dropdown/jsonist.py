from json import dump
import careerapp.models as app

def getJSON(code):
    if code == 'majorgroups':
        members = app.MajorGroup.objects.all()
    else:
        group = app.JobGroup.get(code=code)
        if group.isaMajorGroup():
            members = group.majorgroup.minorgroup_set.all()
        elif group.isaMinorGroup():
            members = group.minorgroup.broadgroup_set.all()
        elif group.isaBroadGroup():
            members = group.broadgroup.job_set.all()

    try:
        members
    except:
        print("That was not a group.")

    memberlist = []
    for member in members:
        memberlist.append(makeDict(member))

    return dump(memberlist)

def makeDict(groupmember):
    d = { "label": groupmember.name, "value": groupmember.code }
    return d
    

