from typing import Dict

def count_characters(word: str) -> Dict[str, int]:
    res: Dict[str, int] = dict()

    for c in word:
        curr_char = str(c)
        if curr_char not in res:
            res[curr_char] = 0

        res[curr_char] += 1
    
    return res


print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
