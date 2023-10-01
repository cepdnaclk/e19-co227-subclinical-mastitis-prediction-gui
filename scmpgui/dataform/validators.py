from django.core.exceptions import ValidationError

def BasicNumeric(value):
    if value.isnumeric():
        return value
    else:
        try:
            flt = float(value)
        except ValueError:
            raise ValidationError("Please enter a number.")