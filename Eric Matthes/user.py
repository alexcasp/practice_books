class User:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        
    def describe_user(self):
        print(f'Это {self.name} ему {self.age} годков и он {self.sex}')
    
    def greet_user(self):
        print(f'Хеллоу {self.name} - мазафакер')
        
user = User('Петька', 18, 'М')
user1 = User('Dfcmrf', 22, '-')

user.describe_user()
user1.describe_user()


# print(user.describe_user())
# print(user1.describe_user())

user.greet_user()
user1.greet_user()

# print(user.greet_user())
# print(user1.greet_user())


