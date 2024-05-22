def month(number, lang):
    ru_months = ['Январь', 'Февраль', 'Март',
            'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь',
            'Октябрь', 'Ноябрь', 'Декабрь']
    en_month = ['January', 'February', 'March',
            'April', 'May', 'June',
            'July', 'August', 'September',
            'October', 'November', 'December']
    if lang == 'ru':
        work_months = ru_months
    elif lang == 'en':
        work_months = en_month
    return work_months[number - 1]
