# 4. Write a script to concatenate N strings.
number=int(input('Input number of string: '))
list_string=[]

for i in range(number):
	list_string.append(input())

all_string = ' '.join(list_string)

print('All strings: ' ,all_string)