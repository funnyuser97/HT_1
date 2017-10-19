
in_data=input()
print('Input  data: ',in_data)
mylist=list(in_data.split(', '))

for i in range(len(mylist)):
	mylist[i]=int(mylist[i])

mytuple=tuple(mylist)

print('Output: ')
print('List: ',mylist)
print('Tuple: ',mytuple)

