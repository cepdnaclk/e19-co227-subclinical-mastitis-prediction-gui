from django.core.exceptions import ValidationError

def StrictNumeric(value):
    val = str(value)
    if val.isnumeric():
        return value
    else:
        raise ValidationError("Please enter a non-negative whole number.",code = "non-numeric")

def CowBreeds(value):
    cow_breeds = ["Angus", "Hereford", "Holstein", "Jersey", "Guernsey", "Limousin", "Charolais", "Simmental", "TexasLonghorn", "Brahman", "Highland", "Shorthorn", "Galloway", "Wagyu", "BelgianBlue", "Dexter", "Chianina", "MurrayGrey", "Piedmontese", "RedPoll", "SantaGertrudis", "MaineAnjou", "Salers", "Normande", "Tarentaise", "Friesian"]
    
    words = value.lower().split()
    
    for word in words:
        if word not in map(str.lower, cow_breeds):
            raise ValidationError(f"'{word}' is not a valid cow breed.")

def phRange(value, min_ph=0, max_ph=14):
    if value < min_ph or value > max_ph:
        raise ValidationError(f"pH must be between {min_ph} and {max_ph}.")