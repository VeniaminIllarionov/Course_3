from utils.utils_operation import last_five_operations, operation_executed, parse_operations_data
from tests.test_operations_list import operations

operation = 'tests.operations.json'


def test_operation_executed():
    assert len(operation_executed(operation)) == 3
    print(operation_executed(operation))
    assert operation_executed(operation) == [{'state': 'EXECUTED'},
                                             {'state': 'EXECUTED'},
                                             {'state': 'EXECUTED'}]

def test_last_five_operations():
    dates = [elem["date"] for elem in last_five_operations(operations)]
    print(dates)
    assert dates == ['2019-11-19T09:22:25.899614',
                     '2019-11-05T12:04:13.781725',
                     '2019-10-30T01:49:52.939296',
                     '2019-08-08T21:58:06.688541',
                     '2019-06-14T19:37:49.044089']


def test_parse_operations_data():
    assert parse_operations_data(operations)
    print(parse_operations_data(operations))
