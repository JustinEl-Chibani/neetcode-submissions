from typing import List

def read_integers() -> List[int]:
    user_input = input()
    list_string = user_input.split(",")
    list_int =[]
    for i in list_string:
        list_int.append(int(i))
    return list_int



# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
