# This is just for testing

class Testing:

    def __init__(self):
        self.__run_tests()

    @staticmethod
    def assert_equal(expect, actual):
        if expect != actual:
            raise Exception('Test Failed!', str(expect) + ' != ' + str(actual))

    def __run_tests(self):
        # Run


Testing()