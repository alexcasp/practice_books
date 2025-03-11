class User:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.login_attempts = 0
        
    def describe_user(self):
        print(f'Это {self.name} ему {self.age} годков и он {self.sex}')
    
    def greet_user(self):
        print(f'Хеллоу {self.name} - мазафакер')
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Попытки входа увеличены до {self.login_attempts}.")
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Количество попыток входа сброшено.")
        
class Privileges:
    def __init__(self, privileges = None):
        if privileges is None:
            privileges = []
        self.privileges = privileges
    
    def show_privileges(self):
        print('\nПривилегии администратора:')
        for privilege in self.privileges:
            print(privilege)
        
        
class Admin(User):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.privileges = Privileges(["разрешено добавлять сообщения", 
                           "разрешено удалять пользователей", 
                           "разрешено банить пользователей"])
        
admin = Admin('Иван', 35, 'Мужской')

admin.describe_user()

admin.privileges.show_privileges()
        
        
        
# user = User('Петька', 18, 'М')
# user1 = User('Dfcmrf', 22, '-')

# user.describe_user()
# user1.describe_user()

# user.greet_user()
# user1.greet_user()

# user.describe_user()
# user1.describe_user()

# user.increment_login_attempts()
# user.reset_login_attempts() 

# user1.increment_login_attempts()
# user1.reset_login_attempts() 

