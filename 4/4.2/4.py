def month(number, lang='ru'):
    months = {
        'ru': ['Январь', 'Февраль', 'Март',
               'Апрель', 'Май', 'Июнь',
               'Июль', 'Август', 'Сентябрь',
               'Октябрь', 'Ноябрь', 'Декабрь'],
        'en': ['January', 'February', 'March',
               'April', 'May', 'June',
               'July', 'August', 'September',
               'October', 'November', 'December']
    }
    return months[lang][number - 1]
