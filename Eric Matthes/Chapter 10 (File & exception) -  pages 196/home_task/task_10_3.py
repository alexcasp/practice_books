a = input('write your name: ')

file_write = '/Users/alex/Documents/Parsultang/Books/Eric Matthes/Chapter 10 (File & exception) -  pages 196/home_task/guests.txt'

with open(file_write, 'w') as file_object:
    file_object.write(a)

with open(file_write) as file_object:
    for line in file_object:
            print(line)
    
# print(file_object)