def StrictNumeric(value):#done
    if value == False:
        return False
    val = str(value)
    if val.isnumeric():
        return value
    else:
        return False

def phRange(value, min_ph=0, max_ph=14):#done
    val = float(value)
    if min_ph <= val <= max_ph:
        return value
    else:
        return False
    
def CowBreeds(value):#done
    val = str(value)
    cow_breeds = ["*","Angus", "Hereford", "Holstein", "Jersey", "Guernsey", "Limousin", "Charolais", "Simmental", "TexasLonghorn", "Brahman", "Highland", "Shorthorn", "Galloway", "Wagyu", "BelgianBlue", "Dexter", "Chianina", "MurrayGrey", "Piedmontese", "RedPoll", "SantaGertrudis", "MaineAnjou", "Salers", "Normande", "Tarentaise", "Friesian"]    
    words = val.lower().split()
    
    for word in words:
        if word not in map(str.lower, cow_breeds):
            return False
        else:
            return value

def required(value):#done
    val =str(value)
    if val and not val.isspace() and val !="None":
        return value
    else:
        return False

   
def Decimal_validator(value, max_digits=10, decimal_places=3):
    val = str(value)

    if '.' in val:
        integer_part, decimal_part = val.split('.')
        if len(integer_part) <= max_digits and len(decimal_part) <= decimal_places and decimal_part.isdigit():
            return value  
    elif val.isnumeric() and len(val) <= max_digits:
        return value  
    
    else:
        return False


def Minvalue_validator(value,min_value=0):
    val = float(value)

    if val >=min_value:
        return value
    else:
        return False

if __name__ == "__main__":
    while True:
        n = str(input("Enter a value or type 'EXIT' to exit: "))
        if n == "EXIT":
            exit()
        else:
            result = Decimal_validator(n)
            print(f"{n} --> {result}")