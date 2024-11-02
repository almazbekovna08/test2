import sqlite3

class DatabaseManager:
    def __init__(self, db_name="users.db"):
        self.connection=sqlite3.connect(db_name)
        self.cursor=self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(30) NOT NULL,
                            age INTEGER NOT NULL
    )
""")
        self.connection.commit()
    
    def add_user(self, user):
        self.cursor.execute("""INSERT INTO users(name, age) VALUES(?, ?)""", (user.name, user.age))
        self.connection.commit()

    def get_user(self, users_id):
        self.cursor.execute("SELECT * FROM users WHERE id=?", (users_id,))
        return self.cursor.fetchone()
    
    def find_user(self, name): #Задание №3
        self.cursor.execute("SELECT * FROM users WHERE name=?", (name,))
        return self.cursor.fetchone()
    
    def delete_user(self, users_id):
        self.cursor.execute("DELETE FROM users WHERE id=?", (users_id,))
        self.connection.commit()
        print("Пользователь удален")


    def close(self):
        self.connection.close()



        



