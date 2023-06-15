
# What we did in office hours not part of lecture

# vehicle1 = {"brand_name": "Nissan", "model":"Skyline","stick":True, "color": "Pearl white"}
vehicle2 = {"brand_name": "Honda","model":"Civic", "stick":True, "color": "Red"} 
vehicle3 = {"brand_name": "Toyota","model":"Supra", "stick":True, "color": "Red"}



# def paint_job(car):
#     print(car['model'])

# print(vehicle1)
import random

class Vehicle:
    win = 100
    def __init__(self, make, model, fight_name, special_move):
        self.make = make
        self.model = model
        self.fight_name = fight_name
        self.mileage = 0
        self.special_move = special_move



    def display_info(self):
        print(f"Make is {self.make}, model: {self.model} color: {self.color}")
        return self
    
    def battle(self, target):
        landed = random.randint(0,1)
        if landed == 1:
            target.mileage += self.special_move["damage"]
            print(f"{self.fight_name} hits {target.fight_name} with {self.special_move['damage']} damage, ouch!")
        else:
            print("You Missed, you can't see me!!")
        
        results = Vehicle.check_mileage(target)
        return results
    
    
    @staticmethod
    def check_mileage(target):
        if target.mileage >= 100:
            return "Winner"








blast = Vehicle("Nissan", "Skyline", "Blast", {"name":"Rocket Blaster", 'damage': 40})

patricia = Vehicle("Chrysler", "PT-Cruiser","Patricia", {"name":"check_engine_light", 'damage': 67})

patricia.battle(blast)

# vehicle2 = Vehicle("Jaguar", "f-type", "orange", 1959, False, 400000)

# vehicle2.display_info()

# print(vehicle1.model)