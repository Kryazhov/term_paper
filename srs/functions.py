import json
from srs.operations import Operation


def load_operations(filename):
    '''загрузка данных из файла json'''
    with open(filename, 'rt', encoding='utf-8') as file:
        data = json.load(file)
    return data


def executed_operations(data):
    '''создание экземпляров из успешных операций'''
    operations = []  # список для добавления экземпляров
    for item in data:  # создание аргументов класса
        if item.get('state') == 'EXECUTED':
            date = item.get('date') or None
            description = item.get('description') or None
            _from = item.get('from') or None
            to = item.get('to') or None
            amount = item.get('operationAmount', {}).get('amount') or None
            name = item.get('operationAmount', {}).get('currency', {}).get('name') or None
            operation = Operation(date, description, _from, to, amount, name)  # создание экземпляра
            operations.append(operation)  # добавление экземпляра
    return operations  # вернет список экземпляров


def printout(sorted_operations):
    out = ''
    for operation in sorted_operations:  # итерации по 5 последним успешным операциям
        if operation._from == None:  # если поле "откуда(from)" - None, не печатаем его вообще
            out += (f'\n{operation.date_conversion(operation.date)} {operation.description}\n'
                         f'{operation.output_formatting(operation.to)}\n{operation.amount} {operation.name}\n')
        else:  # иначе выводим все поля
            out += (f'\n{operation.date_conversion(operation.date)} {operation.description}\n'
                         f'{operation.output_formatting(operation._from)} -> {operation.output_formatting(operation.to)}\n'
                         f'{operation.amount} {operation.name}\n')
    return out
