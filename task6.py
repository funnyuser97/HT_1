# 6. Write a script to check whether a specified value is contained in a group of values. 
mylist = [1, 2, 3, 4, 5]
mytuple= (3, 4, 5, 6, 7)

check_number=int(input('Input check number: '))

print(check_number, '--> ',mylist,' : ',check_number in mylist)
print(check_number, '--> ',mytuple,' : ',check_number in mytuple)
