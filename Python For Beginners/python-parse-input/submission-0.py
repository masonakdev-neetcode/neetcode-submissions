from typing import List

def read_integers() -> List[int]:
    number_str = input()
    str_list = number_str.split(",")
    res: List[int] = list()

    for s in str_list:
        res.append(int(s))
    
    return res


print(read_integers())
print(read_integers())
print(read_integers())
