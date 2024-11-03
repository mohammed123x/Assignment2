
class Invoice:
    def __init__(self, order, customer):
        self.order = order
        self.customer = customer
        self.vat_rate = 0.08

    def generate_invoice(self,loyalty_program):
        '''
        This method will generate the invoice and calculates all the required information,
        applies all the discounts if aplicable and shows the final bill to the user.

        '''
        vat_amount = self.order.total_price * self.vat_rate
        total_with_vat = self.order.total_price + vat_amount
        is_customer_member = loyalty_program.check_customer(self.customer)
        if is_customer_member:
            flat_discount = self.order.total_price * loyalty_program.flat_discount
            total_with_vat = total_with_vat - flat_discount
        else:
            flat_discount = 0

        if is_customer_member and self.order.total_items() >= 5:
            bulk_discount = self.order.total_price * loyalty_program.bulk_purchase_discount
            total_with_vat = total_with_vat - bulk_discount
        else:
            bulk_discount = 0

        invoice = "Invoice for {}\n*** Order Summary ***\n{}\nLoyalty Program Member : {}\n" \
                  "Flat Discount : {}\nBulk Discount : {}\nVAT(8%) : {}\nTotal with VAT : {}".format(self.customer.get_name(),
                                                                                                     self.order.get_order_summary(),
                                                                                                     is_customer_member,
                                                                                                     flat_discount,
                                                                                                     bulk_discount,
                                                                                                     vat_amount,
                                                                                                     total_with_vat)

        return invoice

    def get_vat_rate(self):
        return self.vat_rate

    def set_vat_rate(self,vat):
        self.vat_rate = vat

