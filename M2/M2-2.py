def print_bar_chart(data_dict):
    for key in sorted(data_dict.keys()):
        print (f'{key}|', end = '')
        print (('#'*data_dict[key]) + str(data_dict[key]))






data_dict = {0: 8, 1: 6, 2: 13, 3: 9, 4: 12}
print_bar_chart(data_dict)

data_dict = {8: 15, 7: 17, 6: 10, 5: 8, 4: 12, 3: 13, 2: 11, 1: 9}
print_bar_chart(data_dict)
