def titleType(obj):
    field_typ = " = models.CharField(max_length=100)\n"
    line = obj+field_typ
    return line

def categoryType(obj):
    field_typ = " = models.IntegerField()\n"
    line = obj+field_typ
    return line

def dateType():
    field_typ = "= models.CharField(max_length=100)\n"
    line = obj+field_typ
    return line


    pass

def appType(obj):
    field_typ = " = models.ForeignKey({})\n".format(obj)
    line = obj+field_typ
    return line

def contactType():
    field_typ = " = models.IntegerField()\n"
    line = obj+field_typ
    return line

def phoneType():
    field_typ = "= models.CharField(max_length=100)\n"
    line = obj+field_typ
    return line


    pass

def emailType():
    field_typ = "= models.CharField(max_length=100)\n"
    line = obj+field_typ
    return line


    pass

def numberType(obj):
    field_typ = "= models.FloatField()\n"
    line = obj+field_typ
    return line


    pass

def embedType(obj):
    field_typ = "= models.URLField()\n"
    line = obj+field_typ
    return line


    pass

def imageType():
    field_typ = "= models.ImageField()\n"
    line = obj+field_typ
    return line


    pass

def progressType(obj):
    field_typ = "= models.IntegerField(min_length=0, max_length=100)\n"
    line = obj+field_typ
    return line


    pass

def calculationType():
    field_typ = "= models.CharField(max_length=100)\n"
    line = obj+field_typ
    return line


    pass

def locationType():
    field_typ = "= models.CharField(max_length=100)\n"
    line = obj+field_typ
    return line


    pass

def durationType():
    field_typ = "= models.CharField(max_length=100)\n"
    line = obj+field_typ
    return line


    pass
    
