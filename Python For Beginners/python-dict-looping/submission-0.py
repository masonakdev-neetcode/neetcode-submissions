from typing import Dict, List

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    dict_keys = list()

    for k, v in age_dict.items():
        dict_keys.append(k)
    
    return dict_keys

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    dict_values = list()

    for k, v in age_dict.items():
        dict_values.append(v)
    
    return dict_values


dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
