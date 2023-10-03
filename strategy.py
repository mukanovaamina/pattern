# strategy.py
class PayPalPayment:
    #info about payment
    def pay(self, amount):
        print(f"Payment {amount} with Paypal")

class CreditCardPayment:
    #info about payment
    def pay(self, amount):
        print(f"Payment {amount} with Credit card")

class ShoppingCart:
#accept selected strategy
    def __init__(self, payment_strategy):
        self.products = []
        self.payment_strategy = payment_strategy

#add products
    def add_product(self, product):
        self.products.append(product)

#calculate total
    def checkout(self):
        total = sum(product.price for product in self.products)
        self.payment_strategy.pay(total)


class CosmeticProduct:
    #presenting products
    def __init__(self, name, price):
        self.name = name
        self.price = price