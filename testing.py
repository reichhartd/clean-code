# This is just for testing
from LU import badSmell
from LU.badSmell import orderItem

class Testing:

    def __init__(self):
        self.__run_tests()

    @staticmethod
    def assert_equal(expect, actual):
        if expect != actual:
            raise Exception('Test Failed!', str(expect) + ' != ' + str(actual))

    def __run_tests(self):
        self.__test_create_order()
        self.__test_handle_post_request()

    def __test_create_order(self):
        order_item = orderItem('Test Item')
        order_item.price = 1
        order = badSmell.create_new_order_and_print('Test Order', [order_item], 'ABC', 1.16)
        self.assert_equal(order['name'], 'Test Order')
        self.assert_equal(len(order['items']), 1)
        self.assert_equal(order['items'][0].name, 'Test Item')
        self.assert_equal(order['items'][0].price, 1)
        self.assert_equal(order['items'][0].priceWithTax, 1.16)


    def __test_handle_post_request(self):
        order = badSmell.handlePostRequest({
            'name': 'My Order',
            'items': [
                {
                    'name': 'Milk',
                    'price': 1.15,
                },
                {
                    'name': 'super_special_vat_free_item',
                    'price': 1.50,
                }
            ],
            'buyerId': 'abc123'
        })
        self.assert_equal(order['name'], 'My Order')
        self.assert_equal(len(order['items']), 2)
        self.assert_equal(order['items'][0].name, 'Milk')
        self.assert_equal(order['buyerId'], 'abc123')


Testing()