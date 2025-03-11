file_name = '/Users/alex/Documents/Parsultang/Books/Eric Matthes/Chapter 10 (File & exception) -  pages 196/progamming.txt'

with open(file_name, 'w') as file_object:
    file_object.write('I love programming')
    file_object.write("I love creating new games.")

# with open(file_name) as file_object:
#     for i in file_object:
#         print(i)