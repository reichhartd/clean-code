# This is just for testing
class Testing:

    @staticmethod
    def assert_equal(a, b):
        if a != b:
            raise Exception('Test Failed!', str(a) + ' != ' + str(b))