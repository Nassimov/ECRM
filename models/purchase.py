import json


class Purchase:
    def __init__(self,product_id: str,price: int,currency: str,quantity: int,purchased_at:str):
        self.product_id = product_id
        self.price = price
        self.currency = currency
        self.quantity = quantity
        self.purchased_at = purchased_at
    