# main.py
from singleton import Singleton
from strategy import CreditCardPayment, PayPalPayment, ShoppingCart, CosmeticProduct

# Created instance Singleton
singleton = Singleton()
singleton.some_data = "Some data"

# Creating payment strategy object
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

#created cosmetic products list
product1 = CosmeticProduct("lipstick", 10)
product2 = CosmeticProduct("Shampoo", 15)
product3 = CosmeticProduct("Facemask", 20)

# Created first shopping carts and add products
cart1 = ShoppingCart(credit_card_payment)
cart1.add_product(product1)
cart1.add_product(product2)

# Created second shopping carts and add products
cart2 = ShoppingCart(paypal_payment)
cart2.add_product(product2)
cart2.add_product(product3)

# Make payments for both carts
cart1.checkout()
cart2.checkout()
