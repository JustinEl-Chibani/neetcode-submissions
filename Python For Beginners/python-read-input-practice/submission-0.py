def add_two_numbers() -> int:
    user_input = input()
    num_list = user_input.split(",")
    int_num_list = []
    res=0
    for i in num_list:
        int_num_list.append(int(i))
    return sum(int_num_list)


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
