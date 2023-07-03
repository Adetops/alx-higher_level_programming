import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("John", 'Brad', 5000)
        self.customer2 = Customer('Tina', 'Smith', 3000)

    def test_customer_mail(self):
        self.assertEqual(self.customer1.customer_mail, 'John.Brad@email.com')
        self.assertEqual(self.customer2.customer_mail, 'Tina.Smith@email.com')

    def test_customer_fullname(self):
        self.assertEqual(self.customer1.customer_fullname, 'John Brad')
        self.assertEqual(self.customer2.customer_fullname, 'Tina Smith')

    def test_apply_discount(self):
        self.customer1.apply_discount()
        self.customer2.apply_discount()
        self.assertEqual(self.customer1.purchase, 4750)
        self.assertEqual(self.customer2.purchase, 2850)


if __name__ == '__main__':
    unittest.main()

