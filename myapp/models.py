from django.db import models

# Create your models here.
class feature(models.Model): # by passsing models.Model argument we don't need to wite id it assign automatically each attribute or object an id when it is created
    
    # name: str
    # details: str
    # is_true:bool
    name=models.CharField(max_length=100)#here charfield is act like string
    details=models.CharField(max_length=500)
