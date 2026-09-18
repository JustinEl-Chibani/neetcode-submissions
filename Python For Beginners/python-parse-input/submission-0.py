from typing import List

def read_integers() -> List[int]:
    inp= input()
    listt = inp.split(",")
    intlist=[]
    for i in listt:
        intlist.append(int(i))

    return intlist
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
