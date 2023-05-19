# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(self):
    return self["name"]

def get_total_cash(self):
    return self["admin"]["total_cash"]

def add_or_remove_cash(self, amount):
    self["admin"]["total_cash"] += amount

