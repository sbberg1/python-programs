number_list = [3,5,15,4,11,12,2]
index_value = 0
greater_than_ten_count = 0
loop_times = len(number_list)
while loop_times > 0:
    value_of_number = number_list[index_value]
    if value_of_number > 10:
        greater_than_ten_count = greater_than_ten_count + 1
        index_value = index_value + 1
        loop_times = loop_times - 1
    else:
        index_value = index_value + 1
        loop_times = loop_times - 1
print greater_than_ten_count
    
