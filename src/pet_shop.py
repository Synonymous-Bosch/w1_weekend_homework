# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(self):
    return self["name"]

def get_total_cash(self):
    return self["admin"]["total_cash"]

def add_or_remove_cash(self, amount):
    self["admin"]["total_cash"] += amount

def get_pets_sold(self):
    return self["admin"]["pets_sold"]

def increase_pets_sold(self, pets_sold):
    self["admin"]["pets_sold"] += pets_sold

def get_stock_count(self):
    return len(self["pets"])

def get_pets_by_breed(self, breed):
    pets = []
    for pet in self["pets"]:
        if breed == pet["breed"]:
            pets.append(pet)
    return pets