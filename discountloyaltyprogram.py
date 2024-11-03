
class DiscountLoyaltyProgram():
    flat_discount = 0.10
    bulk_purchase_discount = 0.20

    def __init__(self):
        self.members = []

    def add_member(self,customer):
        self.members.append(customer)

    def check_customer(self,customer):
        res = customer in self.members
        return res

    def get_flat_discount(self):
        return self.flat_discount

    def set_flat_discount(self,fd):
        self.flat_discount = fd

    def get_bulk_purchase_discount(self):
        return self.bulk_purchase_discount

    def set_bulk_purchase_discount(self,bpd):
        self.bulk_purchase_discount = bpd

