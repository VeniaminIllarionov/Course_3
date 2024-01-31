import unittest

from tests.test_operation import operation

from utils.utils_operation import load_operations, operation_executed, last_five_operations, parse_operations_data


class TestOperations(unittest.TestCase):
    def test_operation(self):
        assert load_operations(operation)

    def test_operation_executed(self):
        assert operation_executed(operation)

    def test_last_five_operations(self):
        assert last_five_operations(operation)

    def test_parse_operations_data(self):
        assert parse_operations_data(operation)


if __name__ == '__main__':
    unittest.main()
