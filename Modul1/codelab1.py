random_list = [900, 3.1, 3078, "Hello", 737, "Python", 2.7, 2002, 50,
               "Tech Winter", 7.566, 40, 1, "Is", 60.5, "Better", 1000.1,
               4, "world", 412, 5.5, "AI", 99.234, 12000]

data_tuple = ()
data_list = []
data_dict = {}

for data in random_list:
    if isinstance(data, float):
        data_tuple += (data, )
    elif isinstance(data, str):
        data_list.append(data)
    elif isinstance(data, int):
        
        if data < 10:
            data_dict[data] = "satuan"
        elif data < 100:
            data_dict[data] = "puluhan"
        elif  data < 1000:
            data_dict[data] = "ratusan"
        else:
            data_dict[data] = "ribuan"


print("data dict =", data_dict)
for key, value in data_dict.items():
    print(key, " = ", value)
print("float data tuple = ", data_tuple)
            
print("string data list = ", data_list)
