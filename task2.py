# 2. Write a script to print out a set containing all the colours from color_list_1 which are not present in color_list_2. 
in_data_1=input('Input color_list_1: ')
in_data_2=input('Input color_list_2: ')

color_list_1=set(in_data_1.split(', '))
color_list_2=set(in_data_2.split(', '))

result_list=color_list_1 - color_list_2;

print('Expected output: ')
print(result_list)