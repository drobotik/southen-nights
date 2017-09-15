import unittest
from application.watchman import DataWatchman
from application.rules import RuleOne, RuleTwo, RuleThree

watchman = DataWatchman()
customer = watchman.findCustomer(2)
order = watchman.findOrder(2)

class TestApplicationDiscount(unittest.TestCase):

    def test_order(self):
        self.assertEqual(order.getOrderId(), '2')
        self.assertEqual(order.getCustomerId(), '2')
        self.assertEqual(order.getTotal(), '24.95')
        self.assertEqual(len(order.getItems()), 1)

    def test_customer(self):
        self.assertEqual(customer.getName(), 'Teamleader')
        self.assertEqual(customer.getRevenue(), '1505.95')

    def test_product(self):
        product = order.getItems()[0]
        self.assertEqual(product.getId(), 'B102')
        self.assertEqual(product.getQuantity(), '5')
        self.assertEqual(product.getPrice(), '4.99')
        self.assertEqual(product.getDescription(), 'Press button')
        self.assertEqual(product.getTotal(), '24.95')
    def test_discount(self):
        discounts = list()
        for rule in [ RuleOne(), RuleTwo(), RuleThree() ]:
            if rule.test(order, customer) is True:
                discounts.append(rule.calc(order, customer))
        self.assertEqual(len(discounts), 2)
        self.assertEqual(discounts[0]['discount'], 2.495)
        self.assertEqual(discounts[1][0]['discount'], 'gift')
        self.assertEqual(discounts[1][0]['product_id'], 'B102')