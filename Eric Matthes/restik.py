class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        return f'Рестик называется {self.restaurant_name}'
        return f'В рестике кухня {self.cuisine_type}'
        
    def open_restaurant(self):
        return f'Рестик {self.restaurant_name} открыт'
        
    def restaurant(self):
        return f'В ресторане {self.restaurant_name} cегодня было {self.number_served} посетителей'
    
    def set_number_served(self, served_count):
        if served_count > 0:
            self.number_served = served_count
        else:
            return f'Количество обслуженных посетителей не может быть отрицательным'
        
    def increment_number_served(self, additional_served):
        if additional_served > 0:
            self.number_served += additional_served
        else:
            return f'Невозможно уменьшить число обслуженных посетителей таким образом.'
        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type = 'ice_cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        
    def add_flavors(self, *flavors):
        for flavor in flavors:
            self.flavors.append(flavor)
            
    def display_flavors(self):
        print(f"В киоске с мороженым {self.restaurant_name} доступны следующие вкусы:")
        for flavor in self.flavors:
            print(flavor)

        
rest = Restaurant('Япоснский', 'китайская кухня')
rest1 = Restaurant('Китайский', 'япона кухня')
rest2 = Restaurant('Сербия', 'Сербская кухня')

print(rest.describe_restaurant())
print(rest1.describe_restaurant())
print(rest2.describe_restaurant())

print(f"Текущее количество обслуженных посетителей: {rest.number_served}")

rest.set_number_served(10)
print(f"Теперь количество обслуженных посетителей: {rest.number_served}")

rest.increment_number_served(15)
print(f"После увеличения количество обслуженных посетителей: {rest.number_served}")

ice_cream_stand = IceCreamStand('Мороженое от Дяди Васи')

ice_cream_stand.add_flavors('Ванильное', 'Шоколадное', 'Клубничное')

ice_cream_stand.display_flavors()