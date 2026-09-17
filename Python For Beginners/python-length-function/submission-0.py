def get_longer_word(word1: str, word2: str) -> str:
    len_one = len(word1)
    len_two = len(word2)

    if len_one > len_two or len_one == len_two:
        return word1
    
    return word2

print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
