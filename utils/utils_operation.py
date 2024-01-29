from utils.load_json import load_operations


def operation(filename):
    '''Чтение файла'''
    operations = load_operations('../operations.json')
    return operations


def operation_executed(data):
    '''Поиск одобренных операций'''
    operation_executed_ = []
    operation_equail = operation('../operations.json')
    for i in operation_equail:
        if i.get("state") == "EXECUTED":
            operation_executed_.append(i)
    return operation_executed_


def last_five_operations(operation_execute):
    '''Вывод последних 5-ти опреаций'''
    sorted_operations = sorted(operation_execute, key=lambda x: x["date"], reverse=True)
    last_five = sorted_operations[0:5]
    return last_five


def parse_operations_data(last_five):
    '''Конструктор вывода операций'''
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
