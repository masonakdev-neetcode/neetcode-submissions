def get_substring(input_string: str, start: int, end: int) -> str:
    n = len(input_string)

    if end > n:
        return ""
    
    new_str = ""
    for i in range(start, end):
        new_str += input_string[i]
    
    return new_str

print(get_substring("NeetCode", 1, 7))
print(get_substring("NeetCode", 1, 8))
print(get_substring("NeetCode", 1, 9))
print(get_substring("NeetCode", 0, 2))
print(get_substring("NeetCode", 0, 7))
print(get_substring("NeetCode", 4, 8))
