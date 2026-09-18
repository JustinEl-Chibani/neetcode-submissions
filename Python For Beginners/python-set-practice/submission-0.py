from typing import List

def contains_duplicate(words: List[str]) -> bool:
    set1 = set(words)
    return False if (len(set1) == len(words)) else True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
