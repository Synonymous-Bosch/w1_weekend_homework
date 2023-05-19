import pdb
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
    # pets = []
    # for pet in self["pets"]:
    #     if breed == pet["breed"]:
    #         pets.append(pet)
    # return pets

    return [pet for pet in self["pets"] if breed == pet["breed"]]

def find_pet_by_name(self, name):
    pet_list = [pet for pet in self["pets"] if name == pet["name"]]
    try:
        return pet_list[0]
    except IndexError:
        return None
    
    # pet_list = []
    # for pet in self["pets"]:
    #     if name == pet["name"]:
    #         pet_list.append(pet)
    # if len(pet_list) == 0:
    #     return None
    # else:
    #     return pet_list[0]

def remove_pet_by_name(self, name):
    # for pet in self["pets"]:
    #     if pet["name"] == name:
    #         self["pets"].remove(pet)

    [self["pets"].remove(pet) for pet in self["pets"] if pet["name"] == name]

def add_pet_to_stock(self, new_pet):
    self["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    return False

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet) == True:
        add_or_remove_cash(pet_shop, pet["price"])
        remove_customer_cash(customer, pet["price"])
        increase_pets_sold(pet_shop, 1)
        add_pet_to_customer(customer, pet)
