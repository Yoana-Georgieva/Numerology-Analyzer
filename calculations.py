import datetime

# --- Нумерологична логика ---
master_numbers = [11, 22, 33]

mapping = {
    'A': 1, 'J': 1, 'S': 1,
    'B': 2, 'K': 2, 'T': 2,
    'C': 3, 'L': 3, 'U': 3,
    'D': 4, 'M': 4, 'V': 4,
    'E': 5, 'N': 5, 'W': 5,
    'F': 6, 'O': 6, 'X': 6,
    'G': 7, 'P': 7, 'Y': 7,
    'H': 8, 'Q': 8, 'Z': 8,
    'I': 9, 'R': 9
}

silables_latin = {'A': 1, 'U': 3, 'E': 5, 'O': 6, 'I': 9}

bg_to_lat = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
    'Е': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'Y',
    'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
    'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'H', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH',
    'Щ': 'SHT', 'Ъ': 'A', 'Ь': '', 'Ю': 'YU', 'Я': 'YA'
}

silabels_bg = {'А': 'A', 'Е': 'E', 'И': 'I', 'О': 'O', 'У': 'U', 'Ъ': 'A'}

def reduce_number(num):
    # Смалява числото до едноцифрено, освен ако е мастър число (11, 22, 33).
    while num not in master_numbers and num > 9:
        num = sum(int(digit) for digit in str(num))
    return num

def pitagorian_system(letter):
    # Връща числовата стойност на латинска буква според питагорейската система.
    return mapping.get(letter.upper(), 0)

def transliterate(letter):
    # Превежда една българска буква в латиница според речник.
    return bg_to_lat.get(letter.upper(), '')

def destiny_number(fullname):
    # Изчислява числото на съдбата от пълното име.
    # Работи и с български букви чрез транслитерация.
    total = 0
    for letter in fullname:
        if letter.isalpha():
            if letter in bg_to_lat: # ако е българска буква
                lat = transliterate(letter)
                if lat:
                    total += pitagorian_system(lat[0])
            else:# ако е латинска буква
                total += pitagorian_system(letter)
    return reduce_number(total)

def lifepath_number(birth_date):
    # Изчислява житейския път от дата на раждане (ден + месец + година).
    day = int(birth_date[0])
    month = int(birth_date[1])
    year = int(birth_date[2])
    lifepath = day + month + year
    return reduce_number(lifepath)

def personal_year(birth_date):
    # Изчислява личната година за текущата календарна година (ден + месец + текуща година).
    day = int(birth_date[0])
    month = int(birth_date[1])
    current_year = datetime.datetime.now().year
    your_year = day + month + current_year
    return reduce_number(your_year)

def soul_urge_number(fullname):
    # Изчислява числото на душата.
    # Сумира само гласните в името (български и латински).
    total = 0
    for letter in fullname:
        if letter.isalpha():
            if letter in silabels_bg:
                lat = transliterate(letter)
                if lat:
                    total += pitagorian_system(lat[0])
            elif letter in silables_latin:
                total += pitagorian_system(letter)
    return reduce_number(total)



