class UPI:
    def pay(self):
        print("Payment using UPI")


class Card:
    def pay(self):
        print("Payment using Card")


def payment_method(payment):
    payment.pay()


upi = UPI()
card = Card()

payment_method(upi)
payment_method(card)