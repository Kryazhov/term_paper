import json

def load_operations(filename):
    '''загрузка данных из файла json'''
    with open(filename, 'rt', encoding='utf-8') as file:
        data = json.load(file)
    return data