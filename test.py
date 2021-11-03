# list / array
x = [1, 2, 3]

# print(f"the first value of x list is: {x[0]}")  

# exit()

# for i in x:
#     y = i + 100
    # print(y)

# dictionary
name_dict = {"f_name": "David",
             "l_name": "Chao"}    

for key in name_dict:
    print(f"the key is: {key}")
    print(f"the value is: {name_dict[key]}\n")

# exit()    

for key, value in name_dict.items():
    print(f"{key} :  {value}")