
from datetime import datetime

class Order:
    def __init__(self, cart):
        self.items = cart.get_items()
        self.order_date = datetime.now()
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        '''
        This method will calculate the total price of the books according to their quantity
        ordered by the customer.
        '''
        total = 0
        for item in self.items:
            ebook = item['ebook']
            quantity = item['quantity']
            total += ebook.get_price() * quantity
        return total

    def total_items(self):
        '''
        This method returns the total number of books ordered so that we can check the
        if the bulk discount will be applicable for this customer

        '''
        q = 0
        for item in self.items:
            quantity = item['quantity']
            q += quantity
        return q

    def get_order_summary(self):
        '''
        Returns the summary of the order will the required information.

        '''
        summary = f"Order Date: {self.order_date}\n"
        for item in self.items:
            ebook = item['ebook']
            quantity = item['quantity']
            summary += f"{ebook.get_title()}: {quantity} x {ebook.get_price()}\n"  # Assumes ebook has get_title()
        summary += f"Total: {self.total_price}"
        return summary

    def get_items(self):
        return self.items

    def set_items(self,items):
        self.items = items

    def get_order_date(self):
        return self.order_date

    def set_order_date(self,od):
        self.order_date = od
