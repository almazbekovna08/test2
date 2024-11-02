from task2 import *

class Admin(User, UserServise):
    def __init__(self, name, age):
        super().__init__(name, age)
    

    def __init__(self, db_name="admins.db"):
        self.connection=sqlite3.connect(db_name)
        self.cursor=self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS admins(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(30) NOT NULL,
                            age INTEGER NOT NULL
    )
""")
        self.connection.commit()
        
    def add_admin(self, user):
        self.cursor.execute("""INSERT INTO admins(name, age) VALUES(?, ?)""", (user.name, user.age))
        self.connection.commit()

    def get_admin(self, users_id):
        self.cursor.execute("SELECT * FROM admins WHERE id=?", (users_id,))
        return self.cursor.fetchone()
    
    def delete_admin(self, users_id):
        self.cursor.execute("DELETE FROM admins WHERE id=?", (users_id,))
        self.connection.commit()
        print("Пользователь удален")


    def close(self):
        self.connection.close()

# user_servise=Admin()

# user=Admin(name='Adelina', age=16)
# user_servise.add_admin(user)
# user_servise.get_admin(1)
# user_servise.delete_admin(2)




class Customer(User, UserServise):
    def __init__(self, name, age):
        super().__init__(name, age)
    

    def __init__(self, db_name="customs.db"):
        self.connection=sqlite3.connect(db_name)
        self.cursor=self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS customers(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(30) NOT NULL,
                            age INTEGER NOT NULL
    )
""")
        self.connection.commit()
        
    def add_custom(self, user):
        self.cursor.execute("""INSERT INTO customers(name, age) VALUES(?, ?)""", (user.name, user.age))
        self.connection.commit()

    def get_custom(self, users_id):
        self.cursor.execute("SELECT * FROM customers WHERE id=?", (users_id,))
        return self.cursor.fetchone()
    
    def delete_custom(self, users_id):
        self.cursor.execute("DELETE FROM customers WHERE id=?", (users_id,))
        self.connection.commit()
        print("Пользователь удален")


    def close(self):
        self.connection.close()


# user_servise=Customer()

# user=Customer(name='Adelina', age=16)
# user_servise.add_custom(user)
# user_servise.get_custom(1)
# user_servise.delete_custom(2)







   