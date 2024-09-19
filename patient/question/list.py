# with open('fruits.txt','r') as list.py:
#     all_frutis = fruits_db.read()
#     print(all_frutis)
my_list = ['apple', 'banana', 'mango', 'grape']


user_input = input("Enter a list of words: ")


my_tuple = tuple(my_list)


filename = 'fruits.txt'


with open(filename, 'w') as file:
  
    file.write("List: " + str(my_list) + "\n")
    file.write("Tuple: " + str(my_tuple) + "\n")


with open(filename, 'r') as file:
    contents = file.readlines()
    for line in contents:
        print(contents)
        
        
words_list =input('enter the words to seperated')
words_tuple=tuple(words_list)
print(f'List:{words_list}')
print(f'Tuple:{words_tuple}')

with open('fruits.txt','w')as data_file:
    data_file.write(f'{words_list}\n')
    data_file.write(f'{words_tuple}')
    print("data writen to file")
with open('fruits.txt''r') as data_file:
    line_list = data_file.readline()
    line_tuple = data_file.readline()
    print(line_list)
    print(line_tuple)