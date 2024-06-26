from django.db import models
from django.core.exceptions import ValidationError

def rateValidator(value):
    if value<0:
        raise ValidationError('Value must be greater than or equal to 0.')
    if value > 10:
        raise ValidationError('Value must be less than or equal to 10.')
        
class ratings(models.Model):
    name = models.CharField(max_length=20)
    rate = models.IntegerField(
        validators=[
            rateValidator
        ]
    )
    comments = models.TextField(max_length=100,default='no comment')
    appName = models.TextField(max_length=20,default='unknown')




