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
        
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()    

my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()