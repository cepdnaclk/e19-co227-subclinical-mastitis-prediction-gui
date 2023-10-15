def StrictNumeric(value):
    if value == False:
        return False
    val = str(value)
    if val.isnumeric():
        return value
    else:
        return False

def phRange(value, min_ph=0, max_ph=14):
    if min_ph <= value <= max_ph:
        return value
    else:
        return False
    
def CowBreeds(value):
    cow_breeds = ["*","Angus", "Hereford", "Holstein", "Jersey", "Guernsey", "Limousin", "Charolais", "Simmental", "TexasLonghorn", "Brahman", "Highland", "Shorthorn", "Galloway", "Wagyu", "BelgianBlue", "Dexter", "Chianina", "MurrayGrey", "Piedmontese", "RedPoll", "SantaGertrudis", "MaineAnjou", "Salers", "Normande", "Tarentaise", "Friesian"]    
    words = value.lower().split()
    
    for word in words:
        if word not in map(str.lower, cow_breeds):
            return False
        else:
            return value

def empty_space(value):
    if value and not value.isspace():
        return value
    else:
        return False

def validate_digits(value):
    val = float(value)

    if 0 <= val < 10 ** 10:
        decimal_part = val - int(val)
        if decimal_part == 0 or (decimal_part * 1000).is_integer():
            return value
        
    return False

def validate_freezing_point(value):
    val = float(value)

    if val < 10**10:
        decimal_part = val - int(val)
        if decimal_part == 0 or (decimal_part * 1000).is_integer():
            return value
        
    return False