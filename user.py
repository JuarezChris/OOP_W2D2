import db
from pet import Pet

class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.age = data['age']
        self.money = data['money']
        self.pet = None


    @classmethod
    def get_all_users(cls):
        users = []
        for user in db.users:
            new_user = cls(user)
            new_user.pet = Pet.get_pet_by_id(user['pet'])
            users.append(new_user)

        return users

# print(User.get_all_users())

all_users = User.get_all_users()

print(all_users[0].pet.type)