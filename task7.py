# 7. Write a script to concatenate all elements in a list into a string and print it.
mylist=[1, 'abc', 234, 2345, 'vvb']
print('List: ',mylist)
for i in range(len(mylist)):
	mylist[i]=str(mylist[i])
string=' '.join(mylist)
print('String : ',string)
