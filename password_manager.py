from config import *

def get_auto_passlist(level):
    if level == "1":
        return ["firstlast", "first last","first", "first112233", "first1234567", "first123456789", "first123456", "first12345678", "first1234", "first123"]
    elif level == "2":
        return ["first123", "first@1234", "first@12345", "first786", "first110", "firstlast", "firstlast", "firstlast12", "firstlast123", "firstlast12345", "first@123", "last123", "last12345"]
    elif level == "3":
        return ["firstlast", "first last", "first123", "57273200", "59039200", "234567", "708090", "firstlast", "firstlast123", "firstlast1234", "first123", "first2025", "first@", "first@@", "57273200"]
    elif level == "4":
        return [
                    "19801980", "19811981", "19821982", "19831983", "19841984", "19851985", "19861986", "19871987", "19881988", "19891989",
                    "19901990", "19911991", "19921992", "19931993", "19941994", "19951995", "19961996", "19971997", "19981998", "19991999",
                    "20002000", "20012001", "20022002", "20032003", "20042004", "20052005", "20062006", "20072007", "20082008", "20092009",
                    "20102010", "20112011", "20122012", "20132013", "20142014", "20152015", "20162016", "20172017", "20182018", "20192019",
                    "20202020", "20212021", "20222022", "20232023", "20242024", "20252025", "20262026",
                    "07800780", "07700770", "07500750",
                    "12344321", "12341234", "12345678", "123456", "1234567", "11111234",
                    "@1234@", "@123456@", "@1234567@", "@12345678@", "@@@@1111", "1111@@@@", "@@@@####"
                ]
    else:
        return ["firstlast","first@","first last@@","firstlast12345","firstlast1234","firstlast@@","firstlast@","first@@"]

def generate_password(pw, fn, ln, names):
    pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
    return pas