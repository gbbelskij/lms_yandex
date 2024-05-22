table = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TC',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA',
    'Ъ': '',
    'Ь': ''
}

with open("cyrillic.txt", encoding="UTF-8") as file:
    result = ''
    for string in file:
        for i in string:
            if i in table or i.upper() in table:
                if i.islower():
                    result += table[i.upper()].lower()
                elif i.isupper():
                    if len(table[i]) > 1:
                        result += table[i][:1] + table[i][1:].lower()
                    else:
                        result += table[i]
            else:
                result += i
        with open('transliteration.txt', 'w', encoding='utf-8') as file_out:
            file_out.write(result)
