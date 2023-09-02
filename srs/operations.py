from datetime import datetime

class Operation:
    def __init__(self, date='', description='', _from='', to='', amount='', name=''):
        self.date = date
        self.description = description
        self._from = _from
        self.to = to
        self.amount = amount
        self.name = name

    def date_conversion(self, date):
        '''Преобразование строки даты в нужный формат'''
        date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')  # Преобразование строки в объект datetime
        new_format = date_object.strftime('%d.%m.%Y')  # Преобразование объекта datetime в нужный формат
        return new_format

    def output_formatting(self, account):
        result = ''
        if 'Счет' in account:  # если переданная строка - счет, то формат: Счет **9638
            last_digits = account[-4:]
            result = f'Счет **{last_digits}'
        else:  # иначе карта, формат: Visa Platinum 7000 79** **** 6361
            card_details = account.split()
            card_number = card_details[-1]
            formatted_card_number = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
            result = ' '.join(card_details[:-1]) + ' ' + formatted_card_number
        return result

    def __str__(self):
        return f'{self.date} {self.description} {self._from} {self.to} {self.amount} {self.name}'

    def __repr__(self):
        return f'{self.date} {self.description} {self._from} {self.to} {self.amount} {self.name}'
