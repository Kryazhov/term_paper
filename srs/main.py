from pathlib import Path
from functions import load_operations, executed_operations, printout

operation_json = Path('../operations.json')

data = load_operations(operation_json)  # данные из файла json

executed_operations = executed_operations(data)  # список успешных операций в виде экземпляров (85)

x = int(input('Введите количество операций для вывода, например 5: '))

sorted_operations = sorted(executed_operations, key=lambda x: x.date, reverse=True)[:x]  # x последних операций

print(printout(sorted_operations))


