def remove_fourth_character(word: str) -> str:
    res = ""
    for i in range(0, len(word)):
        if i != 3:
            res += word[i]
    
    return res

print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
