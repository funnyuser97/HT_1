# 10. Write a script to concatenate following dictionaries to create a new one.
dict1={1: 10, 2: 20}
dict2={3: 30, 4: 40}
dict3={5: 50, 6: 60}
dict_res=dict()

dict_res.update(dict1)
dict_res.update(dict2)
dict_res.update(dict3)
print('Input  : ')
print(dict1)
print(dict2)
print(dict3)
print('Output : ',dict_res)