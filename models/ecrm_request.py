import json
from typing import List

from models.purchase import Purchase

class ECRMRequest:
    def __init__(self,salutation: str,last_name:str,first_name:str,email:str,purchases:List[Purchase]):
        self.salutation = salutation
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.purchases = purchases
