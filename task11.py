#11. Write a script to remove duplicates from Dictionary.
dict1={1: 10, 2: 20, 3:10}
values_list = list(set(dict1.values()))

print('Input dictionary',dict1)
print('Values without duplicates : ',values_list)