import sqlite3
from task1 import DatabaseManager
class User:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class UserServise:
    def __init__(self, db_name="users.db"):
        self.db=DatabaseManager(db_name)

    def add_user1(self, user):
        add=self.db.add_user(user)
        if add:
            print("Пользователь успешно добавлен")
        else:
            print('Такой пользователь уже существует')


    def get_user1(self, users_id):
        user_data = self.db.get_user(users_id)
        if user_data:
            return User(name=user_data[1], age=user_data[2])
        else:
            return "Пользователь не найден"
        

    def find_user(self, name): # Задание №3
        user_data = self.db.get_user(name)
        if user_data:
            return User(name=user_data[1], age=user_data[2])
        else:
            return "Пользователь не найден"

        
    def delete_user1(self, users_id):
        delete=self.get_user1(users_id)
        if delete:
            self.db.delete_user(users_id)
        else:
            None


    def close(self):
        self.db.close()


user_servise=UserServise()

user=User(name='Adelina', age=16)
user_servise.add_user1(user)
user_servise.get_user1(1)
user_servise.delete_user1(2)






    




        

