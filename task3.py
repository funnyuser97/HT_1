# 3. Write a script to sum of the first n positive integers.
n_all=int(input('Input amount of numbers: '))
list_numbers=[]

for i in range(n_all):
	list_numbers.append(int(input()))

n_positive=int(input('Input amount of positive numbers for sum: '))	

count=0
s=0
for i in list_numbers:
	if count<n_positive:
		if i>0:
			s=s+i
			count+=1
	else: break

print('Sum of first {0} positive elsement = {1}: '.format(n_positive,s))