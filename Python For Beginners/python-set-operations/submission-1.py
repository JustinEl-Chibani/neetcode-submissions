from typing import List

def count_unique_words(words: List[str]) -> int:
    count = 0
    if not words:
        return 0
    else:
        set_words = set(words)
        list_words = list(set_words)
        return len(list_words)
        
# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
