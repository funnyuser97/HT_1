# 5. Write a script to convert decimal to hexadecimal
string_numbers=input('Input numbers in decimal: ')
list_numbers=list(string_numbers.split(', '))

for i in range(len(list_numbers)):
	list_numbers[i]=hex(int(list_numbers[i])).split('x')[-1]

string_of_hex=', '.join(list_numbers)
print('Input numbers in hexidecimal: ',string_of_hex)
