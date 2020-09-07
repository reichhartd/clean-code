# This File Takes an order via POST request and stores it into the DB

from enum import Enum
from random import randint
from typing import List

tax = 1.16
lastDBId = 0


class ExceptionTypes(Enum):
    DATABASE = 'DATABASE'
    LOGIC = 'LOGIC'


class DBConn:

    def storeUserData(self, user):
        # Karl what are you doing here???
        return self.sqlStore('127.0.0.1', 'username', 'pass', user)

    def storeOrderData(self, order):
        return self.sqlStore('127.0.0.1', 'username', 'pass', order)


    def sqlStore(self, server, username, password, data):
        global lastDBId
        # Not Implemented
        print('Write to DB:')
        success = True
        Error_description = ''

        # Check if an id is duplicated
        if data['id'] == lastDBId:
            success = False
            Error_description = 'Write operation failed: duplicated key error'
            return success, Error_description

        lastDBId = data['id']

        return success, Error_description

    # Returns the last stored orderId
    def get_order_id(self):
        return lastDBId



class OrderItem:
    id: str
    name: str
    price: float
    priceWithTax: float

    def __init__(self, name):
        self.name = name



def createSpecialOrder(special, name, items, tax):
    # loop over all order items and add a tax
    [addTaxToOrderItem(i, tax) for i in items]

    # remove tax from tax free products
    for i in range(len(items)):
        if is_item_vat_free(items[i]):
            items[i].priceWithTax = items[i].price

    dbConn = DBConn()
    order = {'name': name, 'items': items, 'special': special, 'id': dbConn.get_order_id() + 1}
    is_order_valid(order)
    success, description = dbConn.storeOrderData(order)
    if not success:
        raise Exception(ExceptionTypes.DATABASE, description)

    return order

def create_new_order_and_print(name, items: List[OrderItem], buyerId, tax):

    # loop over all order items and add a tax
    [addTaxToOrderItem(i, tax) for i in items]

    # remove tax from tax free products
    for i in range(len(items)):
        if is_item_vat_free(items[i]):
            items[i].priceWithTax = items[i].price

            # 20% Bonus
            if randint(1, 1000) == 1:
                items[i].price = items[i].price * 0.8


    dbConn = DBConn()

    order = {'name': name, 'items': items, 'buyerId': buyerId, 'id': dbConn.get_order_id() + 1}
    is_order_valid(order)
    success, description = dbConn.storeOrderData(order)
    if not success:
        raise Exception(ExceptionTypes.DATABASE, description)

    print('New Order: ' + order['name'] + ' [' + str(order['id']) + ']')
    total = 0
    for i in order['items']:
        print('Item: ' + i.name + ' ' + str(i.priceWithTax) + '€')
        total += i.priceWithTax

    print('Total: ', total, '€')

    return order

# Check if an order is plausible
def is_order_valid(o):
    total = 0
    for i in o['items']:
        total += i.priceWithTax

    if total <= 0:
        raise Exception(ExceptionTypes.LOGIC, 'Total Order price < 0')

def calc_total_order_price(order) -> float:
    total = 0
    for i in order['items']:
        total += i.priceWithTax
    return total


def addTaxToOrderItem(item: OrderItem, tax) -> OrderItem:
    item.priceWithTax = item.price * tax
    return item


def is_item_vat_free(item):
    if item.name == 'post_stamps':
        return True
    elif item.name == 'medicine':
        return True
    elif item.name == 'super_special_vat_free_item':
        return True
    else:
        return False


def handlePostRequest(body):
    """ Gets the data from a client """
    orderName = body['name']
    buyerId = body['buyerId']

    items = []

    i = 0
    for item in body['items']:
        i += 1
        item1 = OrderItem(item['name'])
        item1.price = item['price']
        item1.id = 1
        items.append(item1)

    try:
        return create_new_order_and_print(orderName, items, buyerId, tax)
    except Exception as inst:
        type, desc = inst.args
        if type == ExceptionTypes.DATABASE:
            print('There was a problem with the DB', desc)
        if type == ExceptionTypes.LOGIC:
            print('There was a logic error', desc)
