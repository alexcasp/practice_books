import json

file_name = '/Users/alex/Documents/Parsultang/Books/Eric Matthes/Chapter 10 (File & exception) -  pages 196/Data_Saving/numbers.json'
with open(file_name) as f:
    numbers = json.load(f)
    
print(numbers)