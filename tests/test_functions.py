from srs.functions import executed_operations, printout
from srs.operations import Operation


def test_executed_operations():
    # Создаем тестовые данные
    data = [
        {
            "id": 172864002,
            "state": "EXECUTED",
            "date": "2018-12-28T23:10:35.459698",
            "operationAmount": {
                "amount": "49192.52",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 96231448929365202391"
        },
        {
            "id": 476991061,
            "state": "CANCELED",
            "date": "2018-11-23T17:47:33.127140",
            "operationAmount": {
                "amount": "26971.25",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 7305799447374042",
            "to": "Maestro 3364923093037194"
        },
        {
            "id": 633268359,
            "state": "EXECUTED",
            "date": "2019-07-12T08:11:47.735774",
            "operationAmount": {
                "amount": "2631.44",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 3589276410671603",
            "to": "Счет 96292138399386853355"
        }
    ]

    # Вызываем тестируемую функцию
    result = executed_operations(data)

    # Проверяем, что результат содержит только успешные операции
    assert len(result) == 2

    # Проверяем, что каждый экземпляр имеет правильные атрибуты

    operation1 = result[0]
    assert operation1.date == '2018-12-28T23:10:35.459698'
    assert operation1.description == 'Открытие вклада'
    assert operation1._from == None
    assert operation1.to == 'Счет 96231448929365202391'
    assert operation1.amount == '49192.52'
    assert operation1.name == 'USD'

    operation2 = result[1]
    assert operation2.date == '2019-07-12T08:11:47.735774'
    assert operation2.description == 'Перевод организации'
    assert operation2._from == 'Visa Gold 3589276410671603'
    assert operation2.to == 'Счет 96292138399386853355'
    assert operation2.amount == '2631.44'
    assert operation2.name == 'руб.'


def test_printout():
    operation1 = Operation("2018-03-02T02:03:11.563721", "Открытие вклада", None, "Счет 96231448929365202391", 100,
                           "USD")
    operation2 = Operation("2018-06-12T07:17:01.311610", "Перевод организации", "Visa Classic 4195191172583802",
                           "Visa Platinum 5355133159258236", 200, "EUR")
    operation3 = Operation("2018-11-23T17:47:33.127140", "Перевод со счета на счет", "Счет 33407225454123927865",
                           "Счет 79619011266276091215", 300, "GBP")
    operation4 = Operation("2019-07-12T08:11:47.735774", "Открытие вклада", None, "Счет 17066032701791012883", 400,
                           "CAD")
    operation5 = Operation("2019-09-29T14:25:28.588059", "Перевод организации", "Visa Platinum 2241653116508487",
                           "Счет 26494285169417058486", 500, "AUD")

    operations = [operation1, operation2, operation3, operation4, operation5]

    assert printout(operations) == ('\n'
                                    '02.03.2018 Открытие вклада\n'
                                    'Счет **2391\n'
                                    '100 USD\n'
                                    '\n'
                                    '12.06.2018 Перевод организации\n'
                                    'Visa Classic 4195 19** **** 3802 -> Visa Platinum 5355 13** **** 8236\n'
                                    '200 EUR\n'
                                    '\n'
                                    '23.11.2018 Перевод со счета на счет\n'
                                    'Счет **7865 -> Счет **1215\n'
                                    '300 GBP\n'
                                    '\n'
                                    '12.07.2019 Открытие вклада\n'
                                    'Счет **2883\n'
                                    '400 CAD\n'
                                    '\n'
                                    '29.09.2019 Перевод организации\n'
                                    'Visa Platinum 2241 65** **** 8487 -> Счет **8486\n'
                                    '500 AUD\n')
