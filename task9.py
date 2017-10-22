# 9. Write a script to remove an empty tuple(s) from a list of tuples.
mylist=[(),(),(''),('a'),('a','b'),('a','b','c'),(),()]
print('Input : ',mylist)
i=0
while i<len(mylist):
	if len(mylist[i])==0:
		mylist.remove(mylist[i])
	else: 
		i+=1

print('Output : ',mylist)