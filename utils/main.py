from utils.utils_operation import load_operations, operation_executed, last_five_operations, parse_operations_data


def main():
    executed_data = operation_executed("../operations.json")
    five_operations = last_five_operations(executed_data)
    parsed_operations_list = parse_operations_data(five_operations)
    for operation_message in parsed_operations_list:
        print(operation_message)
        print()


if __name__ == '__main__':
    main()
