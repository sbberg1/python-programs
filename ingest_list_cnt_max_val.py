list_from_user = []	     # Create an empty list
max_value = 0  		     # set the maximum value of list_from_user to 0
max_counter = 0  	     # set the count of maximum value to 0
position_counter = 0
flag = 0
list_size = input("How many numbers in your list?")  # number of inputs
for n in range(list_size):
    input_variable = input("Enter number")
    list_from_user.append(input_variable)
max_value = list_from_user[0]
for n in range(list_size):
    if max_value < list_from_user[n]:
        max_value = list_from_user[n]
for n in range(list_size):
    if max_value == list_from_user[n]:
        max_counter = max_counter +1
for n in range(list_size):
    if max_value == list_from_user[n]:
        if flag == 0:
            position_counter = n
            flag = flag +1
print position_counter
print max_value
print max_counter
    
