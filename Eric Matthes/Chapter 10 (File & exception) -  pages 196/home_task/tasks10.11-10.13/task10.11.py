import json

# Имя файла
file = 'lknum.json'

# Получаем ввод от пользователя
vvod = input('Vvod from user: ')
# Инициализируем numbers перед try-except
numbers = []

 # Читаем существующие данные или используем пустой список
try:
    with open(file, 'r') as f:
        numbers = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    numbers = [] # Если файла нет или он пустой, используем пустой список

if not isinstance(numbers, list):
    numbers = [numbers]
# Если numbers не список (например, строка от предыдущей версии), преобразуем в список

numbers.append(vvod)
# Добавляем новое число в список
with open(file, 'w') as f:
    json.dump(numbers, f)
# Записываем обновленный список обратно в файл
print(f'Mazafuku {numbers}')