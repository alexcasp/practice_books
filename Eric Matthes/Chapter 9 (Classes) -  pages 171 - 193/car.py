class Car():
    '''Простая модель авто'''
    
    def __init__(self, make, model, year):
        '''атрибуты описания автомобиля'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        '''возвращаем отформатированое описание'''
        long_name = f' {self.make} {self.model} {self.year}'
        return long_name.title()
    
    def read_odometer(self):
        '''Выводит пробег машины в милях'''
        print(f'This car has {self.odometer_reading} miles on it.')
        
    def update_odometer(self, mileage):
        '''Устанавливает на одометре заданное значение.
           При попытке обратной подкрутки изменение отклоняется.'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        '''Увеличивает показания одометра с заданным приращением.'''
        self.odometer_reading += miles
        
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()    

# my_new_car = Car('audi', 'q7', 2006)

# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

class Battery():
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")
    
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f'This car can go about {range} miles on a full charge.')

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def fill_gas_tank():
        print(f"This car doesn't need a gas tank!")
        
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100


# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


