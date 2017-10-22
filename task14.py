# 14. Write a script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
dict1=dict()
count=int(input('Input top value: '))
for i in range(count):
	dict1[i+1]=(i+1)*(i+1)
	
print('Input : ',dict1)
