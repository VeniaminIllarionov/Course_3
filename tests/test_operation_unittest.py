import unittest

from tests.test_operation import operations

from utils.utils_operation import operation, operation_executed, last_five_operations, parse_operations_data


class TestOperations(unittest.TestCase):
    def test_operation(self):
        assert operation(operations)

    def test_operation_executed(self):
        assert operation_executed(operations)

    def test_last_five_operations(self):
        assert last_five_operations(operations)

    def test_parse_operations_data(self):
        assert parse_operations_data(operations)


if __name__ == '__main__':
    unittest.main()
