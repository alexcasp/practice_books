# import os
# # print(os.getcwd())
# with open('/Users/alex/Documents/Parsultang/Books/Eric Matthes/Chapter 10 (File & exception) -  pages 196/pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)

file_name = '/Users/alex/Documents/Parsultang/Books/Eric Matthes/Chapter 10 (File & exception) -  pages 196/pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
    
# for line in lines:
#     print(line.rstrip())
    
#построение одной строки со всеми цифрами

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input()
if birthday in pi_string:
    print('Yes, it is')
else:
    print('Oh, no')
    
# print(f"{pi_string[:52]}...")
# print(len(pi_string))
    