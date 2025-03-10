class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f'Рестик называется {self.restaurant_name}')
        print(f'В рестике кухня {self.cuisine_type}')
        
    def open_restaurant(self):
        print(f'Рестик {self.restaurant_name} открыт')
        
rest = Restaurant('Япоснский', 'китайская кухня')
rest1 = Restaurant('Китайский', 'япона кухня')
rest2 = Restaurant('Сербия', 'Сербская кухня')

rest.describe_restaurant()
# rest.open_restaurant()

print(rest.describe_restaurant())
print(rest1.describe_restaurant())
print(rest2.describe_restaurant())
# print(rest.open_restaurant())