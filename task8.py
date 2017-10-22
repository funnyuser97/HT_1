# 8. Write a script to replace last value of tuples in a list. 
mylist=[(1,2,3),(3,4,5),(6,7,8)]
number=int(input('Input value for change :'))
print('Input : ',mylist)

for i in range(len(mylist)):
	tmp_list=list(mylist[i])
	tmp_list[-1]=number
	mylist[i]=tuple(tmp_list)

print('Output : ',mylist)
