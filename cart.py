
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, ebook, quantity=1):
        for item in self.items:
            if item['ebook'] == ebook:
                item['quantity'] += quantity
                return
        # If ebook not in cart, add as new entry
        self.items.append({'ebook': ebook, 'quantity': quantity})

    def remove_item(self, ebook):
        # Removes the ebook if it's in the cart
        self.items = [item for item in self.items if item['ebook'] != ebook]

    def update_quantity(self, ebook, quantity):
        # Updates quantity for the ebook if it exists in the cart
        for item in self.items:
            if item['ebook'] == ebook:
                item['quantity'] = quantity
                return

    def get_items(self):
        # Returns a list of items in the cart
        return self.items

    def clear_cart(self):
        # Empties the cart
        self.items = []
