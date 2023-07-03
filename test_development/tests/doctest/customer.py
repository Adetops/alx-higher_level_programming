class Customer:
    """
    A sample customer class

    >>> customer1 = Customer('John', 'Brad', 5000)
    >>> customer2 = Customer('Tina', 'Smith', 3000)
    >>> customer1.customer_mail
    'John.Brad@email.com'
    >>> customer2.customer_mail
    'Tina.Smith@email.com'
    >>> customer2.customer_fullname
    'Tina Smith'
    >>> customer1.customer_fullname
    'John Brad'
    >>> customer1.apply_discount()
    4750
    >>> customer2.apply_discount()
    2850
    """

    discount = 0.95
    def __init__(self, first_name, last_name, purchase):
        self.first = first_name
        self.last = last_name
        self.purchase = purchase

    @property
    def customer_mail(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def customer_fullname(self):
        return f"{self.first} {self.last}"

    def apply_discount(self):
        self.purchase = int(self.purchase * self.discount)
        return self.purchase


if __name__ == '__main__':
    import doctest
    doctest.testmod()
