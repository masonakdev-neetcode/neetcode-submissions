from typing import List

def count_unique_words(words: List[str]) -> int:
    seen = set()

    for w in words:
        seen.add(w)
    
    return len(seen)


print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
