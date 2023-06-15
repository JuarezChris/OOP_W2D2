import db

class Pet:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.type = data["type"]
        self.age = data["age"]

    @classmethod
    def get_pet_by_id(cls, id):
        for pet in db.pets:
            if pet['id'] == id:
                new_pet = cls(pet)
                return new_pet
