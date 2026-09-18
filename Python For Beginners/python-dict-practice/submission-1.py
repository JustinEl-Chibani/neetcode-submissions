from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dict_char = {}
    for char in word:
        if char not in dict_char:
            dict_char[char] = 1
        else:
            dict_char[char] +=1
            
    return dict_char


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
