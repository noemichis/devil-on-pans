from datetime import date
from django.core.exceptions import ValidationError

def date_validation(value):
    today = date.today()
    if value < today:
        raise ValidationError('Sorry, we can not go back in time..')