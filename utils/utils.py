from utils import load_json


def operation():
    '''# Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.'''
    operations = load_json.load_operations()
    return operations


def operation_executed(data):
    operation_executed_ = []
    operation_equail = operation()
    for i in operation_equail:
        # print(i)
        if i.get("state") == "EXECUTED":
            operation_executed_.append(i)
    return operation_executed_


def last_five_operations(operation_execute):
    sorted_operations = sorted(operation_execute, key=lambda x: x["date"], reverse=True)
    last_five = sorted_operations[0:5]
    return last_five


def parse_operations_data(last_five):
    operation_data = []
    for operation in last_five:
        date = operation.get('date')[0:10]
        formatted_date = '.'.join(date.split('-')[::-1])
        description = operation.get('description')
        operations_amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        card_to = operation.get('to').split()[-1]
        card_type_to = ' '.join(operation.get('to').split()[:-1])
        star_card_to = '*' * 2 + card_to[-4:]
        if operation.get("from") is None:
            card_type_from = "No_Name"
            star_card_from = ""
        else:
            card_type_from = ' '.join(operation.get('from').split()[:-1])
            card_number = operation.get('from').split()[-1]
            star_card_from = f' {card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}'

        operation_data.append(f'''{formatted_date} {description}
{card_type_from}{star_card_from} -> {card_type_to} {star_card_to}
{operations_amount} {currency}''')

    return operation_data
