
from discountloyaltyprogram import DiscountLoyaltyProgram
from ebook import EBook
from order import Order
from customer import Customer
from cart import Cart
from invoice import Invoice

program = DiscountLoyaltyProgram()

# Creating the EBook instances
ebook1 = EBook("Python Basics", "John Doe", "2023-01-01", "English", 29.99, 300)
ebook2 = EBook("Advanced Python", "Jane Smith", "2023-05-12", "English", 39.99, 400)
ebook3 = EBook("Data Science with Python", "Mike Lee", "2022-08-20", "English", 49.99, 500)
ebook4 = EBook("Machine Learning Essentials", "Sara Kim", "2024-02-15", "English", 59.99, 550)
ebook5 = EBook("AI for Beginners", "Chris Brown", "2023-09-30", "English", 24.99, 250)

# creating a customer object
customer2 = Customer(2, "Customer 2", "Dubai", "555-1234")

# creating a cart for the customer
cart_2 = Cart()
# adding books into the cart fo the customer
cart_2.add_item(ebook3, 1)
cart_2.add_item(ebook4, 3)
cart_2.add_item(ebook5, 2)

# creating the order for the customer using their cart
order = Order(cart_2)

# creating the invoice for the order
invoice = Invoice(order, customer2)

# displaying the order invoice
print(invoice.generate_invoice(program))